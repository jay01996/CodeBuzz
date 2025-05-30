from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(University)
admin.site.register(College)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Semester)
admin.site.register(Section)
admin.site.register(Group)