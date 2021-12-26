from django.urls import re_path
from apps.sensor import views

urlpatterns = [
    re_path(r"^room_sensor_list/$", views.list_room_sensors, name="list_room_sensor"),
    re_path(r"^room_sensor_data/(?P<pk>\d+)/$", views.room_sensor_data, name="room_sensor_data"),
]
