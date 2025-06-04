from django.db import models
from institute.models import Course, Semester, Branch, Department  # Adjust import paths as per your project

class Syllabus(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    subject = models.CharField(max_length=200)
    program_number = models.CharField(max_length=50)
    program_description = models.TextField()

    def __str__(self):
        return f"{self.subject} ({self.program_number}) - {self.semester}"
    