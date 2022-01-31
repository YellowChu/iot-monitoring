from apps.sensor.models import RoomSensor
from apps.sensor.serializers import RoomSensorSerializer, RoomSensorUplinksSerializer

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet


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


class RoomSensorUplinksViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = RoomSensorUplinksSerializer
    queryset = RoomSensor.objects.all().order_by("id")
