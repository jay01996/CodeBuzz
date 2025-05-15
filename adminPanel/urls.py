from django.urls import path
from .views import admin_profile

urlpatterns = [
    path('profile/', admin_profile, name='admin_profile'),
]
