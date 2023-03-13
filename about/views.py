from django.shortcuts import render , redirect
from django.contrib.auth.models import User,auth

def about(request):

    return render(request,'about.html')