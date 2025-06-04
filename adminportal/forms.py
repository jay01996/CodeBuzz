from django import forms
from accounts.models import Student, Faculty
from .models import FacultySubjectAssignment


class StudentUpdateForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Student
        fields = [
            'university', 'college', 'department', 'course', 'branch', 'semester',
            'section', 'group', 'roll_no', 'full_name', 'email', 'contact_number',
            'gender', 'dob', 'address', 'profile_photo'
        ]


class FacultySubjectAssignmentForm(forms.ModelForm):
    class Meta:
        model = FacultySubjectAssignment
        fields = ['faculty', 'subject', 'branch', 'semester', 'section']
        widgets = {
            'section': forms.TextInput(attrs={'placeholder': 'A, B, C...'})
        }
