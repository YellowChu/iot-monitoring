from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import RoomSensor


def list_room_sensors(request):
    room_sensors = list(RoomSensor.objects.all().values("pk", "device_id", "device_name", "device_description"))

    return JsonResponse({"room_sensors": room_sensors})


def room_sensor_data(request, pk):
    room_sensor = get_object_or_404(RoomSensor, pk=pk)
    sensor_data_list = []
    print(pk)
    if int(pk) == 2:
        print("?")
        sensor_data_list = [{
            "time": "2022-01-16T09:30:12.028Z",
            "pressure": 99435.75,
            "temperature": 23.431564331054688,
            "battery": 4.691720485687256
        }]
    else:
        for uplink in room_sensor.uplinks.all():
            pressure, temperature, battery = room_sensor.parse_uplink_payload(uplink.payload)
            sensor_data = {
                "time": uplink.received_at or uplink.created,
                "pressure": pressure,
                "temperature": temperature,
                "battery": battery, 
            }
            sensor_data_list.append(sensor_data)
    
    print(sensor_data_list)
    return JsonResponse({"sensor_data_list": sensor_data_list})
