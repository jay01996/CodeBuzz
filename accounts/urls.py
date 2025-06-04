from .views import *
from django.urls import path

# This file defines the URL patterns for the accounts app, mapping URLs to their respective 
# It includes paths for student, faculty, and admin profiles, dashboards, and logout functionalities.

urlpatterns = [
    
    path('student-profile/', student_profile, name='student_profile'),
    path('student-logout/',student_logout, name='student_logout'),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
    
    path('faculty-profile/', faculty_profile, name='faculty_profile'),
    path('faculty-logout/',faculty_logout, name='faculty_logout'),
    path('faculty-dashboard/', faculty_dashboard, name='faculty_dashboard'),
    
    path('admin-profile/', admin_profile, name='admin_profile'),
    path('admin-logout/',admin_logout, name='admin_logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    
    path('my-class/', faculty_my_class, name='faculty_my_class'),
    path('problems/', faculty_problems, name='faculty_problems'),
    path('assignments/', faculty_assignments, name='faculty_assignments'),
    path('review-submissions/', faculty_review_submissions, name='faculty_review_submissions'),
    path('student-stats/', faculty_student_stats, name='faculty_student_stats'),
    path('leaderboard/', faculty_leaderboard, name='faculty_leaderboard'),
    path('class-test/', faculty_class_test, name='faculty_class_test'),
    path('contests/', faculty_contests, name='faculty_contests'),
    path('problem-bank/', faculty_problem_bank, name='faculty_problem_bank'),
    path('notifications/', faculty_notifications, name='faculty_notifications'),
    
    
    
]
