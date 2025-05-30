from django.db import models


# institute/models.py

class University(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=255)
    established_year = models.PositiveIntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class College(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='colleges')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    principal_name = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(blank=True, null=True)

    class Meta:
        unique_together = ('university', 'code')

    def __str__(self):
        # return f"{self.name} ({self.university.name})"
        return self.name


class Department(models.Model):
    college = models.ForeignKey('College', on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    hod_name = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('college', 'code')

    def __str__(self):
        # return f"{self.name} - {self.college.name}"
        return self.name

class Course(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    duration_years = models.PositiveIntegerField(default=4)

    class Meta:
        unique_together = ('department', 'code')

    def __str__(self):
        # return f"{self.name} ({self.department.name})"
        return self.name

class Branch(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)

    class Meta:
        unique_together = ('course', 'code')

    def __str__(self):
        # return f"{self.name} - {self.course.name}"
        return self.name

class Semester(models.Model):
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, related_name='semesters')
    number = models.PositiveSmallIntegerField(help_text="Semester number (1-8)")

    class Meta:
        unique_together = ('branch', 'number')
        ordering = ['number']

    def __str__(self):
        # return f"Semester {self.number} - {self.branch.name}"
        return str(self.number)

class Section(models.Model):
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=10)  # e.g., A, B, C

    class Meta:
        unique_together = ('semester', 'name')

    def __str__(self):
        # return f"Section {self.name} - {self.semester}"
        return self.name

class Group(models.Model):
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('name', 'section')
    def __str__(self):
        # return f"{self.name} - {self.section}"
        return self.name
