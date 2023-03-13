from django.urls import path
from . import views

urlpatterns = [
    path('candid', views.candid, name='candid'),   
]
