from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import *


urlpatterns = [
    
    # Basic Core Apps
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),   
    path('vision_mission/', vision_mission, name='vision_mission'),
    path('verify_email/', verify_email, name='verify_email'),
    path('set_password/', set_password, name='set_password'),
    path('login/', user_login, name='login'),
    
    path('problems/', include('problems.urls')),
    path('performance/', include('performance.urls')),
    path('academics/', include('academics.urls')),
    path('institute/', include('institute.urls')),
    path('adminportal/', include('adminportal.urls')),

    # Include the accounts app URLs
    # This will include all the URLs defined in accounts/urls.py
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]



# Static & Media Files in Development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
