from django.contrib import admin
from django.urls import path
from core.views import *


urlpatterns = [
   
    path('contact/',contact, name='contact'),
    path('about/', about, name='about'),
    path('vision_mission/', vision_mission, name='vision_mission'),
]
