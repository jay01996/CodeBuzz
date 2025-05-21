from django.urls import path
from .views import syllabus_view

urlpatterns = [
    path('syllabus/', syllabus_view, name='syllabus'),
]
