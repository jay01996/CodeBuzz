from django.shortcuts import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from accounts.models import *
import json



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


def vision_mission(request):
    return render(request, 'vision_mission.html')

def verify_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            student = StudentProfile.objects.get(email=email)
            request.session['reset_email'] = student.email  # Store in session
            return redirect('set_password')
        except StudentProfile.DoesNotExist:
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
            student = StudentProfile.objects.get(email=email)
            student.password = password1
            student.save()
            request.session.flush()
            messages.success(request, 'Password successfully updated!')
            return redirect('login') 
    return render(request, 'set_password.html')


def user_login(request):
    email = ''
    role = ''
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if role == 'student':
            try:
                student = Student.objects.get(email=email)
                if student.password == password:
                    request.session['student_id'] = student.id
                    request.session['role'] = role  # store role in session
                    return redirect('student_dashboard')
                else:
                    messages.error(request, "Incorrect password.")
            except Student.DoesNotExist:
                messages.error(request, "No student found with this email.")

        elif role == 'faculty':
            try:
                faculty = Faculty.objects.get(email=email)
                if faculty.password == password:
                    request.session['faculty_id'] = faculty.id
                    request.session['role'] = role  # store role in session
                    return redirect('faculty_dashboard')
                else:
                    messages.error(request, "Incorrect password.")
            except Faculty.DoesNotExist:
                messages.error(request, "Faculty Not Found")

        elif role == 'admin':
            try:
                admin = Admin.objects.get(email=email)
                if admin.password == password:
                    request.session['admin_id'] = admin.id
                    request.session['role'] = role  # store role in session
                    return redirect('admin_dashboard')
                else:
                    messages.error(request, "Incorrect password.")
            except Admin.DoesNotExist:
                messages.error(request, "Admin Not Found")
                
        # if user is not None and hasattr(user, 'student'):
        # login(request, user)
        # request.session['is_student'] = True  # 🔥 Set session key
        # return redirect('student_dashboard')

    return render(request, 'login.html', {'email': email, 'role': role})
