from django.urls import path
from . import views

urlpatterns = [
    path('babyshoot', views.babyshoot, name='babyshoot'),   
]
