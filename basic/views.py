from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
def home(request):
    room=Room.objects.all()
    return render(request,"home.html",{'room':room})
def room(request):
    return render(request,"rav.html")