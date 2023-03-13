from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

def contact(request):

   

    return render(request,'contact.html')