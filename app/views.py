from django.http import HttpResponse
from django.shortcuts import render
from .models import Room,CustomUser
# Create your views here.
def home(request):
    obj=Room.objects.all()
    print(obj)
    return HttpResponse("success")

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]



        print(username,email,password1,password2)
        if password1==password2:
            obj=CustomUser()
            obj.username=username
            obj.email=email
            obj.password=password1
            obj.save()

        else:
            print("Password mismatch!")

        return render(request,"home.html")

    else:
        return render(request,"login.html")

def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]



        print(email,password)
        obj=CustomUser.objects.get(email=email)
        if obj.password==password:
             return render(request,"home.html")
        else:
            print("Email and Password are wrong")

    else:
        return render(request,"login.html")