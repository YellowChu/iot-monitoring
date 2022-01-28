from apps.sensor.models import RoomSensor
from apps.sensor.serializers import RoomSensorSerializer

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class RoomSensorViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = RoomSensorSerializer
    queryset = RoomSensor.objects.all().order_by("id")
