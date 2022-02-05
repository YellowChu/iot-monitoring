import json
import logging
import paho.mqtt.client as mqtt
import random
import sys
from dateutil.parser import isoparse
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.conf import settings

from apps.sensor.models import Uplink, Gateway, RoomSensor

# USER = "bp-lora-nguyen@ttn"
USER = f"{settings.TTN_APP_NAME}@ttn"
PASSWORD = settings.TTN_API_KEY
PUBLIC_TLS_ADDRESS = settings.TTN_MQTT_TLS_ADDRESS
PUBLIC_TLS_ADDRESS_PORT = settings.TTN_MQTT_TLS_ADDRESS_PORT
DEVICE_ID = settings.TTN_DEVICE_ID
ALL_DEVICES = True
QOS = 0


def notify_about_uplink():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "sensor",
        {
            "type": "send_message",
            "message": "New uplink"
        }
    )


def parse_uplink_message(msg_payload):
    payload_dict = json.loads(msg_payload)

    device_id = payload_dict.get("end_device_ids", {}).get("device_id", "")
    uplink_message = payload_dict.get("uplink_message", {})
    uplink_gateways = uplink_message.get("rx_metadata", [])

    uplink_payload = uplink_message.get("frm_payload", "")
    received_at = uplink_message.get("received_at", "")
    spreading_factor = uplink_message.get("settings", {}).get("data_rate", {}).get("lora", {}).get("spreading_factor", None)
    consumed_airtime_str = uplink_message.get("consumed_airtime", "")
    consumed_airtime = None
    if consumed_airtime_str:
        consumed_airtime = float(consumed_airtime_str[:-1])

    uplink = Uplink.objects.create(
        payload=uplink_payload,
        received_at=isoparse(received_at),
        spreading_factor=spreading_factor,
        consumed_airtime=consumed_airtime,
    )

    for gateway in uplink_gateways:
        gateway_id = gateway.get("gateway_ids", {}).get("gateway_id", "")
        gateway_eui = gateway.get("gateway_ids", {}).get("eui", "")

        gateway = Gateway.objects.filter(gateway_id=gateway_id).first()
        if not gateway:
            gateway = Gateway.objects.create(gateway_id=gateway_id, gateway_eui=gateway_eui)
        
        gateway.uplinks.add(uplink)

    room_sensor, _ = RoomSensor.objects.get_or_create(device_id=device_id)
    room_sensor.uplinks.add(uplink)

    notify_about_uplink()


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    # print("\nMessage received on topic '" + message.topic + "' with QoS = " + str(message.qos))
    print("Got uplink", message.topic)
    msg_type = message.topic.split("/")[-1]
    if msg_type == "join":
        print("device joined")
    elif msg_type == "up":
        print("uplink received")
        parse_uplink_message(message.payload)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("\nConnected successfully to MQTT broker")
    else:
        print("\nFailed to connect, return code = " + str(rc))


def stop(client):
    client.disconnect()
    sys.exit(0)


# mid = message ID
def on_subscribe(client, userdata, mid, granted_qos):
    print("\nSubscribed with message id (mid) = " + str(mid) + " and QoS = " + str(granted_qos))


def on_disconnect(client, userdata, rc):
    print("\nDisconnected with result code = " + str(rc))


def on_log(client, userdata, level, buf):
    print("\nLog: " + buf)
    logging_level = client.LOGGING_LEVEL[level]
    logging.log(logging_level, buf)


def start_mqtt_broker():
    # Generate client ID with pub prefix randomly
    client_id = f'python-mqtt-{random.randint(0, 1000)}'

    print("Create new mqtt client instance")
    mqttc = mqtt.Client(client_id)

    print("Assign callback functions")
    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe
    mqttc.on_message = on_message
    mqttc.on_disconnect = on_disconnect
    # mqttc.on_log = on_log  # Logging for debugging OK, waste

    # Setup authentication from settings above
    mqttc.username_pw_set(USER, PASSWORD)

    # IMPORTANT - this enables the encryption of messages
    mqttc.tls_set()  # default certification authority of the system

    print("Connecting to broker: " + PUBLIC_TLS_ADDRESS + ":" + str(PUBLIC_TLS_ADDRESS_PORT))
    mqttc.connect(PUBLIC_TLS_ADDRESS, PUBLIC_TLS_ADDRESS_PORT, 60)


    if ALL_DEVICES:
        print("Subscribe to all topics (#) with QoS = " + str(QOS))
        mqttc.subscribe("#", QOS)
    elif len(DEVICE_ID) != 0:
        topic = "v3/" + USER + "/devices/" + DEVICE_ID + "/up"
        print("Subscribe to topic " + topic + " with QoS = " + str(QOS))
        mqttc.subscribe(topic, QOS)
    else:
        print("Can not subscribe to any topic")
        stop(mqttc)

    print("And run forever")
    try:
        run = True
        while run:
            mqttc.loop(10)  # seconds timeout / blocking time
    except KeyboardInterrupt:
        stop(mqttc)
