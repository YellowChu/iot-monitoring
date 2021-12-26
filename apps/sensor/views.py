from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import RoomSensor


def list_room_sensors(request):
    room_sensors = list(RoomSensor.objects.all().values("pk", "device_id"))

    return JsonResponse({"room_sensors": room_sensors})


def room_sensor_data(request, pk):
    room_sensor = get_object_or_404(RoomSensor, pk=pk)
    sensor_data_list = []
    for uplink in room_sensor.uplinks.all():
        pressure, temperature, battery = room_sensor.parse_uplink_payload(uplink.payload)
        sensor_data = {
            "time": uplink.received_at or uplink.created,
            "pressure": pressure,
            "temperature": temperature,
            "battery": battery, 
        }
        sensor_data_list.append(sensor_data)
    
    return JsonResponse({"sensor_data_list": sensor_data_list})
