from django.urls import re_path

from apps.sensor import views

urlpatterns = [
    re_path(r"^schedule_downlink/$", views.schedule_downlink, name="schedule_downlink"),
]
