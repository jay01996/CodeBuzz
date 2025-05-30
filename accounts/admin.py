from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import *


admin.site.register(Student) 
admin.site.register(Faculty)
admin.site.register(Admin)
