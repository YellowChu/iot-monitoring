import codecs
import csv
import json
import pytz
import requests
from dateutil.parser import parse as parse_date
from datetime import datetime, timedelta, time

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from rest_framework.authtoken.models import Token

from apps.sensor.models import RoomSensor, DailyDownlinksCount


# TODO: make function decorator
def token_authorized(request):
    token_key = request.META["HTTP_AUTHORIZATION"]
    token_key = token_key.replace("Token ", "")
    token = Token.objects.filter(key=token_key).first()
    if token and token.user:
        return True
    else:
        return False


def schedule_downlink(request):
    if token_authorized(request):
        sf_dr = {
            "SF7": "05",
            "SF8": "04",
            "SF9": "03",
            "SF10": "02",
            "SF11": "01",
            "SF12": "00",
            "Unchanged": "06",
        }
        
        spreading_factor = request.GET.get("spreading_factor", "Unchanged")
        color_code = request.GET.get("color_code", "Unchanged")

        payload_sf = sf_dr.get(spreading_factor, "06")
        if color_code == "Unchanged":
            payload_led = "0000"
        else:
            payload_led = "0001" + color_code

        payload = payload_sf + payload_led
        payload = codecs.encode(codecs.decode(payload, "hex"), "base64").decode()

        url = settings.TTN_DL_URL
        post_bearer = settings.TTN_POST_BEARER
        body = {
            "downlinks": [{
                "frm_payload": payload,
                "f_port": 1,
                "confirmed": True,
            }]
        }

        response = requests.post(url, data=json.dumps(body), headers={"Authorization": post_bearer})

        if response.status_code == 200:
            room_sensor = RoomSensor.objects.filter(device_id="lopy4-otaa").first()
            today = timezone.now()
            tomorrow = today + timedelta(1)
            today_start = datetime.combine(today, time())
            today_end = datetime.combine(tomorrow, time())

            today_downlink_count = DailyDownlinksCount.objects.filter(
                date__lte=today_end,
                date__gte=today_start,
                room_sensor=room_sensor
            ).first()
            if not today_downlink_count:
                DailyDownlinksCount.objects.create(downlink_count=1, room_sensor=room_sensor)
            else:
                today_downlink_count.downlink_count += 1
                today_downlink_count.save()
            return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "ttn_nok"})
    else:
        return JsonResponse({"status": "user_nok"})


def export_room_sensor_uplinks(request, pk):
    if token_authorized(request):
        room_sensor = RoomSensor.objects.filter(pk=pk).first()
        if not room_sensor:
            return JsonResponse({"status": "user_nok"})

        from_date = request.GET.get("export_from", "")
        to_date = request.GET.get("export_to", "")
        export_temp = request.GET.get("export_temp", False)
        export_pres = request.GET.get("export_pres", False)

        export_temp = True if export_temp == "true" else False
        export_pres = True if export_pres == "true" else False
        if not export_temp and not export_pres:
            return JsonResponse({"status": "req_nok"})

        if not from_date:
            from_datetime = room_sensor.uplinks.last().received_at
        else:
            from_datetime = parse_date(from_date)
            from_datetime = pytz.timezone("Europe/Prague").localize(from_datetime)

        if not to_date:
            to_datetime = room_sensor.uplinks.first().received_at
        else:
            to_datetime = parse_date(to_date)
            to_datetime = pytz.timezone("Europe/Prague").localize(to_datetime)

        # prepare csv
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="room_sensor_export.csv"'},
        )

        headers = ["Date time"]
        if export_temp:
            headers.append("Temperature [°C]")
        if export_pres:
            headers.append("Pressure [kPa]")

        writer = csv.writer(response)
        writer.writerow(headers)

        uplinks = room_sensor.uplinks.filter(received_at__range=[from_datetime, to_datetime])

        for uplink in uplinks:
            pressure, temperature, _ = room_sensor.parse_uplink_payload(uplink.payload)
            row = [uplink.received_at.strftime("%d.%m.%Y %H:%M")]
            if export_temp:
                row.append(round(temperature, 2))
            if export_pres:
                row.append(round((pressure / 1000), 2))
            
            writer.writerow(row)
        
        return response
    else:
        return JsonResponse({"status": "user_nok"})
