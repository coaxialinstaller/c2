from django.contrib import admin
from django.urls import path

from core.views import (
    upload,
    alive_service,
    control,
)


urlpatterns = [
    path('upload', upload),
    path("alive_service", alive_service),
    path("control", control)
]