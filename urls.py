from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include
from django.views.generic import TemplateView

import views

import urls_api
from apps.sensor import urls as sensor_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^auth-api/", include("djoser.urls")),
    re_path(r"^auth-api/", include("djoser.urls.authtoken")),

    re_path(r"^api/v1/", include(urls_api)),
    re_path(r"^sensor/", include(sensor_urls)),

    re_path(r"^token-auth/", views.token_authorized),
    re_path(r"^(?!admin).*$", TemplateView.as_view(template_name="base.html")),
]
