from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', faculty_profile, name='faculty_profile'),
    path('logout/',faculty_logout, name='faculty_logout')
]
