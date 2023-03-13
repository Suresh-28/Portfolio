from django.urls import path
from . import views

urlpatterns = [
    path('wedding', views.wedding, name='wedding'),   
]
