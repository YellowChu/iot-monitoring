from email.mime import base
from apps.sensor.views_api import CarTrackerViewSet, MailboxNotifierViewSet, RoomSensorViewSet, RoomSensorDashboardViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"roomsensor", RoomSensorViewSet, basename="roomsensor")
router.register(r"roomsensordashboard", RoomSensorDashboardViewSet, basename="roomsensordashboard")
router.register(r"mailboxnotifier", MailboxNotifierViewSet, basename="mailboxnotifier")
router.register(r"cartracker", CarTrackerViewSet, basename="cartracker")

urlpatterns = router.urls
