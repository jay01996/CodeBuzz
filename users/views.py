from django.shortcuts import render, redirect
from users.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from faculty.models import Faculty
from adminPanel.models import Admin
import json


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


def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')
    student = Student.objects.get(id=student_id)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']  # or dynamic based on data
    monthly_scores = [65, 75, 80, 85, 90]
    overall_percent = sum(monthly_scores) // len(monthly_scores)
    context = {
        'student': student,
        'solved_count': 12,
        'pending_assignments': 3,
        'overall_score': 86,
        'rank': 18,
        'months': json.dumps(months),
        'monthly_scores': json.dumps(monthly_scores),
        'overall_percent': overall_percent
        
    }
    return render(request, 'student_dashboard.html', context)



# def student_dashboard(request):
#     student_id = request.session.get('student_id')
#     if not student_id:
#         return redirect('login')

#     student = Student.objects.get(id=student_id)

#     # Fake stats for now (integrate real logic later)
#     context = {
#         'student': student,
#         'solved_count': 12,
#         'pending_assignments': 3,
#         'overall_score': 86,
#         'rank': 18,
#     }
#     return render(request, 'students_dashboard.html', context)


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