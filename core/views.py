
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
import os

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

def control(request):
    return render(request, "control.json")