import codecs
import json
import requests

from django.http import JsonResponse


def schedule_downlink(request):
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

    url = "https://eu1.cloud.thethings.network/api/v3/as/applications/bp-lora-nguyen/devices/lopy4-otaa/down/push"
    post_bearer = "Bearer NNSXS.JEKRGRH35KVSALXFA5OOXB6FFLWEOIDUHDW3PGQ.I5C3D3X2QXVRYJMQERNNVNMDEO3VCB7QM5J6JI7DNHUSOGFGOEVQ"
    body = {
        "downlinks": [{
            "frm_payload": payload,
            "f_port": 1,
            "confirmed": True,
        }]
    }

    response = requests.post(url, data=json.dumps(body), headers={"Authorization": post_bearer})
    print(response.content)

    if response.status_code == 200:
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status": "nok"})
