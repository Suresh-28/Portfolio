from django.shortcuts import render , redirect
from . models import Childshoot

def babyshoot(request):

    baby=Childshoot.objects.all()

    return render(request,'babyshoot.html', {'baby': baby})