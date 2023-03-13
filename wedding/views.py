from django.shortcuts import render , redirect
from . models import Weedshoot
def wedding(request):



    wed=Weedshoot.objects.all()

    return render(request,'wedding.html',{'wed': wed})