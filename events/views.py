from django.shortcuts import render , redirect
from . models import Eventshoot

def events(request):

    eve=Eventshoot.objects.all()


    return render(request,'events.html',{'eve': eve})