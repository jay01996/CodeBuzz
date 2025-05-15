from django.urls import path
from .views import faculty_profile

urlpatterns = [
    path('profile/', faculty_profile, name='faculty_profile'),
]
