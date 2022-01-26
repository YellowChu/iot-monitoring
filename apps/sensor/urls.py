from django.urls import re_path
from apps.sensor import views

urlpatterns = [
    re_path(r"^ws_test/$", views.ws_send),
]
