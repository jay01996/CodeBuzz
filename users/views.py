from django.shortcuts import render, redirect
from users.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
            messages.error(request, "Faculty module not implemented yet.")
        elif role == 'admin':
            messages.error(request, "Admin module not implemented yet.")
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
