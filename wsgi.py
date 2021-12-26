"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Subscribe to TTN MQTT Server
from threading import Thread
from apps.sensor.mqtt import start_mqtt_broker
thread = Thread(target=start_mqtt_broker)
thread.start()

application = get_wsgi_application()
