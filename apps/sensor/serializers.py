from random import randint
from datetime import datetime, timedelta, time

from django.utils import timezone
from rest_framework import serializers

from apps.sensor.models import CarTracker, DailyDownlinksCount, MailboxNotifier, RoomSensor


class RoomSensorSerializer(serializers.ModelSerializer):
    sensor_data_list = serializers.SerializerMethodField()
    uplinks_count = serializers.SerializerMethodField()
    displayed_uplinks_count = serializers.SerializerMethodField()

    class Meta:
        model = RoomSensor
        fields = [
            "id",
            "device_id",
            "device_name",
            "device_description",
            "sensor_data_list",
            "uplinks_count",
            "displayed_uplinks_number",
            "displayed_uplinks_count",
            "display_temperature",
            "display_pressure",
        ]

    def get_sensor_data_list(self, room_sensor):
        sensor_data_list = []

        if room_sensor.displayed_uplinks_number == None:
            uplinks = room_sensor.uplinks.all()
        else:
            uplinks = room_sensor.uplinks.all()[:room_sensor.displayed_uplinks_number]

        for uplink in uplinks:
            pressure, temperature, battery = room_sensor.parse_uplink_payload(uplink.payload)
            sensor_data = {
                "time": uplink.received_at or uplink.created,
                "pressure": pressure,
                "temperature": temperature,
                "battery": battery, 
            }
            sensor_data_list.append(sensor_data)

        return sensor_data_list

    def get_uplinks_count(self, room_sensor):
        return room_sensor.uplinks.count()

    def get_displayed_uplinks_count(self, room_sensor):
        if room_sensor.displayed_uplinks_number == None:
            return room_sensor.uplinks.count()
        else:
            return room_sensor.displayed_uplinks_number


class RoomSensorDashboardSerializer(serializers.ModelSerializer):
    uplinks_data = serializers.SerializerMethodField()
    last_battery_reading = serializers.SerializerMethodField()
    last_sf_reading = serializers.SerializerMethodField()
    downlink_count = serializers.SerializerMethodField()
    gateway_count = serializers.SerializerMethodField()

    class Meta:
        model = RoomSensor
        fields = [
            "id",
            "uplinks_data",
            "last_battery_reading",
            "last_sf_reading",
            "downlink_count",
            "gateway_count",
        ]
    
    def get_uplinks_data(self, room_sensor):
        uplinks = room_sensor.uplinks.filter(
            received_at__gte=timezone.now().replace(hour=0, minute=0, second=0),
            received_at__lte=timezone.now().replace(hour=23, minute=59, second=59)
        )

        uplink_data = [
            {
                "received_at": uplink.received_at or uplink.created,
                "spreading_factor": uplink.spreading_factor,
                "consumed_airtime": uplink.consumed_airtime,
            } 
            for uplink in uplinks
        ]
        return uplink_data

    def get_last_battery_reading(self, room_sensor):
        last_uplink = room_sensor.uplinks.first()
        if last_uplink:
            _,_, battery = room_sensor.parse_uplink_payload(last_uplink.payload)
            return battery
        else:
            return None

    def get_last_sf_reading(self, room_sensor):
        last_uplink = room_sensor.uplinks.first()
        if last_uplink:
            return last_uplink.spreading_factor
        else:
            return None
    
    def get_downlink_count(self, room_sensor):
        downlink_count = DailyDownlinksCount.objects.filter(
            date__gte=timezone.now().replace(hour=0, minute=0, second=0),
            date__lte=timezone.now().replace(hour=23, minute=59, second=59),
            room_sensor=room_sensor
        ).first()
        if not downlink_count:
            return 0
        else:
            return downlink_count.downlink_count

    def get_gateway_count(self, room_sensor):
        uplinks = room_sensor.uplinks.filter(
            received_at__gte=timezone.now().replace(hour=0, minute=0, second=0),
            received_at__lte=timezone.now().replace(hour=23, minute=59, second=59)
        )

        gateway_count = {}
        for uplink in uplinks:
            for gateway in uplink.gateway_set.all():
                gateway_count[gateway.gateway_id] = gateway_count.get(gateway.gateway_id, 0) + 1

        return gateway_count


class MailboxNotifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailboxNotifier
        fields = [
            "id",
            "device_id",
            "device_name",
            "device_description",
            "number_of_mails",
            "should_notify",
            "emails",
        ]


class CarTrackerSerializer(serializers.ModelSerializer):
    locations_data_list = serializers.SerializerMethodField()

    class Meta:
        model = CarTracker
        fields = [
            "id",
            "device_id",
            "device_name",
            "device_description",
            "locations_data_list",
        ]

    def get_locations_data_list(self, car_tracker):
        location_data_list = []

        uplinks = car_tracker.uplinks.all()[:10]

        for uplink in uplinks:
            latitude, longtitude = car_tracker.parse_uplink_payload()
            sensor_data = {
                "time": uplink.received_at or uplink.created,
                "latitude": latitude,
                "longtitude": longtitude,
            }
            location_data_list.append(sensor_data)

        return location_data_list
