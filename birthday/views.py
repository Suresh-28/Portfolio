from django.shortcuts import render , redirect
from . models import Destination1

def birthday(request):

    dests1=Destination1.objects.all()

    return render(request,'birthday.html', {'dests1': dests1})