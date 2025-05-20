"""
URL configuration for CodeBuzz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import *
from users.views import *
from faculty.views import *
from adminPanel.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('about/', about, name='about'),
    path('contact/', contact, name ='contact'),
    path('student_dashboard/', student_dashboard, name ='student_dashboard'),
    path('faculty_dashboard/', faculty_dashboard, name ='faculty_dashboard'),
    path('admin_dashboard/', admin_dashboard, name ='admin_dashboard'),
    path('student/', include('users.urls')),
    path('faculty/', include('faculty.urls')),
    path('admin/', include('adminPanel.urls')),
    path('reset-password/', verify_email, name='verify_email'),
    path('set-password/', set_password, name='set_password'),
    path('admin/', admin.site.urls)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
