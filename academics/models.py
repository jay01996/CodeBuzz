from django.db import models


class Syllabus(models.Model):
    course = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    subject = models.CharField(max_length=200)
    program_number = models.CharField(max_length=10)
    program_description = models.TextField()
    branch = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject} - Sem {self.semester}"