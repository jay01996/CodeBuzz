from django.contrib import admin
from django.urls import path
from users.views import *


urlpatterns = [
    path('logout/', student_logout, name='student_logout'),
    path('profile/', student_profile, name='student_profile'),
]
