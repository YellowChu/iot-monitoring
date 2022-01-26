from apps.sensor.models import RoomSensor

from rest_framework import serializers


class RoomSensorSerializer(serializers.ModelSerializer):
    sensor_data_list = serializers.SerializerMethodField()

    class Meta:
        model = RoomSensor
        fields = ["id", "device_id", "device_name", "device_description", "sensor_data_list"]

    def get_sensor_data_list(self, room_sensor):
        sensor_data_list = []
        if room_sensor.pk == 2:
            sensor_data_list = [{
                "time": "2022-01-16T09:30:12.028Z",
                "pressure": 99435.75,
                "temperature": 23.431564331054688,
                "battery": 4.691720485687256
            }]
        else:
            for uplink in room_sensor.uplinks.all()[:10]:
                pressure, temperature, battery = room_sensor.parse_uplink_payload(uplink.payload)
                sensor_data = {
                    "time": uplink.received_at or uplink.created,
                    "pressure": pressure,
                    "temperature": temperature,
                    "battery": battery, 
                }
                sensor_data_list.append(sensor_data)
        print(sensor_data_list)
        return sensor_data_list
