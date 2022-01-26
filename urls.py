from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include
from django.views.generic import TemplateView

import urls_api
from apps.sensor import urls as sensor_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^api/v1/", include(urls_api)),
    re_path(r"^sensor/", include(sensor_urls)),
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html")),
]
