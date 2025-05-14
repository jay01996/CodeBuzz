from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    password = models.CharField(max_length=100)  # We'll hash it later if needed

    # ✅ Extra field for tracking
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

