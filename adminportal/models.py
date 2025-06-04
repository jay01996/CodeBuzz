from django.db import models
from institute.models import *  # Adjust import paths as per your project
from django.contrib.auth import get_user_model
from accounts.models import Faculty, Admin  # adjust import as needed


class Subject(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    
    subject_code = models.CharField(max_length=20, unique=True)
    subject_name = models.CharField(max_length=100)
    subject_type = models.CharField(max_length=50, choices=(('Theory', 'Theory'), ('Practical', 'Practical')))
    credits = models.IntegerField()
    
    class Meta:
        unique_together = ('department', 'course', 'branch', 'semester', 'subject_code')

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"

# syllabus/models.py


User = get_user_model()

class Syllabus(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="syllabi")
    program_number = models.CharField(max_length=20)
    program_title = models.CharField(max_length=255)
    program_description = models.TextField()
    difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    marks = models.PositiveIntegerField()
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('subject', 'program_number')
        ordering = ['subject', 'program_number']

    def __str__(self):
        return f"{self.subject.subject_code} - P{self.program_number}: {self.program_title}"


class FacultySubjectAssignment(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    added_by = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('faculty', 'subject', "course", 'branch', 'semester', 'section', 'group')
        ordering = ['faculty', 'subject']

    def __str__(self):
        return f"{self.faculty.user.get_full_name()} - {self.subject.subject_code} ({self.branch.name} {self.semester.number}{self.section})"
