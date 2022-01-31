from email.mime import base
from apps.sensor.views_api import RoomSensorViewSet, RoomSensorUplinksViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"roomsensor", RoomSensorViewSet, basename="roomsensor")
router.register(r"roomsensoruplinks", RoomSensorUplinksViewSet, basename="roomsensoruplinks")

urlpatterns = router.urls
