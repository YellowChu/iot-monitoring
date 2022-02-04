from django.http import HttpResponse, JsonResponse

from rest_framework.authtoken.models import Token


def token_authorized(request):
    token_key = request.META["HTTP_AUTHORIZATION"]
    token_key = token_key.replace("Token ", "")
    token = Token.objects.filter(key=token_key).first()
    if token and token.user:
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status": "nok"})
