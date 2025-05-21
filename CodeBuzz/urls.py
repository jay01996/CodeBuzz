from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import home, about, contact, verify_email, set_password
from users.views import student_dashboard, user_login
from faculty.views import faculty_dashboard
from adminPanel.views import admin_dashboard

urlpatterns = [
    # Public Pages
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    # Dashboards
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    path('faculty/dashboard/', faculty_dashboard, name='faculty_dashboard'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),

    # Password Management
    path('reset-password/', verify_email, name='verify_email'),
    path('set-password/', set_password, name='set_password'),

    # Role-specific Apps
    path('student/', include('users.urls')),
    path('faculty/', include('faculty.urls')),
    path('admin-panel/', include('adminPanel.urls')),

    # Features
    path('submissions/', include('submissions.urls')),
    path('performance/', include('performance.urls')),

    # Django Admin Panel
    path('admin/', admin.site.urls),
]

# Static & Media Files in Development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
