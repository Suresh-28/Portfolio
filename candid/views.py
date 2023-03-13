from django.shortcuts import render , redirect
from . models import Candidshoot

def candid(request):

    can=Candidshoot.objects.all()


    return render(request,'candid.html',{'can': can})