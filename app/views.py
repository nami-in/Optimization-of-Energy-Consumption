from django.http import HttpResponse
from django.shortcuts import render
from .models import Room
# Create your views here.
def home(request):
    obj=Room.objects.all()
    print(obj)
    return HttpResponse("success")

def login(request):
    return render(request,'login.html')