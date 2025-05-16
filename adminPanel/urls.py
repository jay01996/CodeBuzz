from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', admin_profile, name='admin_profile'),
    path('admin_logout/', admin_logout, name='admin_logout')
]
