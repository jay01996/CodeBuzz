from django.contrib import admin
from .models import Subject, Syllabus, FacultySubjectAssignment  # Adjust the import path as per your project structure

admin.site.site_header = "Admin Portal"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to the Admin Portal"  

# You can register your models here if needed
admin.site.register(Subject)
admin.site.register(FacultySubjectAssignment)

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['subject', 'program_number', 'program_title', 'difficulty_level', 'marks']
    search_fields = ['subject__subject_name', 'program_number', 'program_title']
    list_filter = ['difficulty_level', 'subject']
