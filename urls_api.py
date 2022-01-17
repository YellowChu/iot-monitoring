from apps.sensor.views_api import RoomSensorViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"roomsensor", RoomSensorViewSet)

urlpatterns = router.urls
