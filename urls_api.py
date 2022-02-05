from email.mime import base
from apps.sensor.views_api import RoomSensorViewSet, RoomSensorDashboardViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"roomsensor", RoomSensorViewSet, basename="roomsensor")
router.register(r"roomsensordashboard", RoomSensorDashboardViewSet, basename="roomsensordashboard")

urlpatterns = router.urls
