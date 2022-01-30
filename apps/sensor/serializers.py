from random import randint

from apps.sensor.models import RoomSensor

from rest_framework import serializers


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
        if room_sensor.device_id == "test":
            sensor_data_list = [
                {
                    "time": "2022-01-16T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-17T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-18T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-19T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-20T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-21T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-22T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-23T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-24T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-25T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-26T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-27T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-28T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-29T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-30T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-01-31T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-02-01T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-02-02T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-02-03T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
                {
                    "time": "2022-02-04T09:30:12.028Z",
                    "pressure": randint(100, 120),
                    "temperature": randint(20, 30),
                    "battery": 4.691720485687256
                },
            ]
        else:
            if room_sensor.displayed_uplinks_number == None:
                qs = room_sensor.uplinks.all()
            else:
                qs = room_sensor.uplinks.all()[:room_sensor.displayed_uplinks_number]

            for uplink in qs:
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
