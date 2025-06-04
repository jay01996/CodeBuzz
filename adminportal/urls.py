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
    path('update-student/<student_id>/', update_student, name='update_student'),

    path('update-faculty/<faculty_id>/', update_faculty, name='update_faculty'),
    path('delete-faculty/<int:faculty_id>/', delete_faculty, name='delete_faculty'),
    path('add-faculty/', add_faculty, name='add_faculty'),

    
    path('ajax/load-branches/', load_branches, name='ajax_load_branches'),
    path('ajax/load-semesters/', load_semesters, name='ajax_load_semesters'),
    path('ajax/load-sections/', load_sections, name='ajax_load_sections'),
    path('ajax/load-groups/', load_groups, name='ajax_load_groups'),
    
    path('manage-subjects/', manage_subjects, name='manage_subjects'),
    # path('update-subject/<int:subject_id>/', update_subject, name='update_subject'),
    path('delete-subject/<int:subject_id>/', delete_subject, name='delete_subject'),
    
    path('manage-syllabus/', manage_syllabus, name='manage_syllabus'),
    path('delete-syllabus/<int:syllabus_id>/', delete_syllabus, name='delete_syllabus'),
    
    path('manage-faculty-assignments', manage_faculty_assignments, name='manage_faculty_assignments'),


]
