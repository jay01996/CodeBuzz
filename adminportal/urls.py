from django.urls import path
from .views import *

urlpatterns = [
    path('manage-students/', manage_students, name='manage_students'),
    path('manage-problem/', manage_problem, name='manage_problem'),
    path('display-ranking/', display_ranking, name='display_ranking'),
    path('view-reports/', view_reports, name='view_reports'),
    path('manage-syllabus/', manage_syllabus, name='manage_syllabus'),
    path('create_announcement/', create_announcement, name='create_announcement'),
    path('email-students/', email_students, name='email_students'),
    path('student-logs/', student_logs, name='student_logs'),
    path('manage-faculty/', manage_faculty, name='manage_faculty'),
    path('admin/update-student/<int:student_id>/', update_student, name='update_student'),

]
