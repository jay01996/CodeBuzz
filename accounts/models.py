from django.db import models
from django.utils import timezone
from institute.models import *

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

# === Student Table ===
class Student(models.Model):
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    student_id = models.CharField(max_length=15, unique=True, editable=False)
    roll_no = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, default='01234')
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='student_photos/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.student_id:
            last = Student.objects.order_by('-id').first()
            new_number = (int(last.student_id[3:]) + 1) if last and last.student_id else 1
            self.student_id = f'CBS{str(new_number).zfill(6)}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.student_id})"

# === Faculty Table ===
class Faculty(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, default='01234')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=100)
    qualifications = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.full_name} ({self.employee_id})"

# === Admin Table ===
class Admin(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, default='01234')
    designation = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.full_name} ({self.designation})"