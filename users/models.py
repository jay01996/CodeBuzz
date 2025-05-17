from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone_no = models.CharField(max_length=15)
#     department = models.CharField(max_length=50)
#     batch = models.CharField(max_length=20)
#     session = models.CharField(max_length=20)
#     course = models.CharField(max_length=50)
#     semester = models.CharField(max_length=10)
#     section = models.CharField(max_length=10)
#     password = models.CharField(max_length=100)  # We'll hash it later if needed

#     # ✅ Extra field for tracking
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} ({self.email})"



class StudentManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        student = self.model(email=email, **extra_fields)
        student.set_password(password)
        student.save(using=self._db)
        return student

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(email, password, **extra_fields)


class Student(AbstractBaseUser):
    student_id = models.CharField(max_length=10, unique=True, editable=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    dob = models.DateField(null=True, blank=True)
    
    # Profile photo
    profile_photo = models.ImageField(upload_to='student_photos/', null=True, blank=True)

    university = models.CharField(max_length=100, null=True, blank=True)
    college = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    branch = models.CharField(max_length=100, null=True, blank=True)
    semester = models.IntegerField(null=True, blank=True)
    section = models.CharField(max_length=10, null=True, blank=True)

    contact_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(max_length=500, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = StudentManager()

    def __str__(self):
        return self.full_name
    
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def save(self, *args, **kwargs):
        if not self.student_id:
            last_id = Student.objects.all().order_by('id').last()
            if last_id:
                new_id = int(last_id.student_id[3:]) + 1
            else:
                new_id = 1
            self.student_id = f'CBS{str(new_id).zfill(7)}'
        super().save(*args, **kwargs)

    @property
    def is_staff(self):
        return self.is_admin
