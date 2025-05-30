from django.db import models
from accounts.models import Student
# Create your models here.

class RankRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)
    problems_solved = models.IntegerField(default=0)
    last_submission = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-total_score']

    def __str__(self):
        return f"{self.student.user_id} - Score: {self.total_score}"