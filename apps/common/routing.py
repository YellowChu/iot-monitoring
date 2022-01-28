from django.urls import re_path

from apps.common import consumers

websocket_urlpatterns = [
    re_path(r"ws/sensor/$", consumers.SensorConsumer.as_asgi())
]