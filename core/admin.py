from django.contrib import admin
from users.models import Student
from faculty.models import Faculty
from adminPanel.models import Admin

admin.site.register(Student),
admin.site.register(Faculty)
admin.site.register(Admin)
