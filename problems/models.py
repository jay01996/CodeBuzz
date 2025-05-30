from django.db import models

from accounts.models import Student  # adjust as per your actual user model
from datetime import timedelta, date

class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    problem_name = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.problem_name}"

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    assigned_to = models.ManyToManyField(Student, related_name='assigned_problems')
    assigned_date = models.DateField(auto_now_add=True)

    @property
    def deadline(self):
        return self.assigned_date + timedelta(days=3)

    def __str__(self):
        return self.title

class PracticeProblem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.title
