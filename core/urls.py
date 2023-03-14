from django.contrib import admin
from django.urls import path

from core.views import (
    upload,
    control,
)


urlpatterns = [
    path('upload', upload),
    path("control", control)
]