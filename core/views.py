from django.shortcuts import *
from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import Student  # Use your custom or default user model
from django.contrib.auth.hashers import make_password


# Create your views here.
# def home(request):
#     return render(request, 'homepage.html')


def home(request):
    role = request.session.get('role')
    if role == 'student' and request.session.get('student_id'):
        return redirect('student_dashboard')
    elif role == 'faculty' and request.session.get('faculty_id'):
        return redirect('faculty_dashboard')
    elif role == 'admin' and request.session.get('admin_id'):
        return redirect('admin_dashboard')
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def verify_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            student = Student.objects.get(email=email)
            request.session['reset_email'] = student.email  # Store in session
            return redirect('set_password')
        except Student.DoesNotExist:
            messages.error(request, 'Email not found. Please enter a valid registered email.')

    return render(request, 'verify_email.html')


# Step 2: Set new password view
def set_password(request):
    email = request.session.get('reset_email')
    if not email:
        return redirect('verify_email')

    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
        else:
            student = Student.objects.get(email=email)
            # student.password = make_password(password1)
            student.password = password1
            student.save()
            # messages.success(request, 'Password successfully updated!')
            request.session.flush()
            messages.success(request, 'Password successfully updated!')
            return redirect('login') 
            # return redirect('login')  # Replace with your login page name
           
    return render(request, 'set_password.html')