"""
ASGI config for project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from threading import Thread

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from apps.common import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "settings.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(routing.websocket_urlpatterns)
    )
})

# Subscribe to TTN MQTT Server
from apps.common.mqtt import start_mqtt_broker

thread = Thread(target=start_mqtt_broker)
thread.start()
