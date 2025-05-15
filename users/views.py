from django.shortcuts import render, redirect
from users.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from faculty.models import Faculty
from adminPanel.models import Admin


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
                    return redirect('admin_dashboard')
                else:
                    messages.error(request, "Incorrect password.")
            except Admin.DoesNotExist:
                messages.error(request, "admin Not Found")
    return render(request, 'login.html', {'email': email, 'role': role})

def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')
    student = Student.objects.get(id=student_id)
    return render(request, 'student_dashboard.html', {'student': student})

def student_logout(request):
    request.session.flush()
    return redirect('home')


def student_profile(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')  # session not found = redirect to login
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return redirect('login')

    context = {
        'student': student,
    }
    return render(request, 'student_profile.html', context)