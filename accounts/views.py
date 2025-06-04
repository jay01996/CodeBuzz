from django.shortcuts import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json


# Create your views here.

def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')  # session not found = redirect to login
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return redirect('login')
    
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
    return render(request, 'student/student_dashboard.html', context)


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
    return render(request, 'student/student_profile.html', context)



# Create faculty views here.
def faculty_dashboard(request):
    faculty_id = request.session.get('faculty_id')
    
    if not faculty_id:
        return redirect('login')
    try:
        admin = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        # If admin with the given ID is not found, redirect to login
        return redirect('login')
    
    features = [
        {"title": "My Class", "description": "List of students and their performance", "url": "faculty_my_class"},
        {"title": "Problems Section", "description": "Assign today's problems and check pending ones", "url": "faculty_problems"},
        {"title": "Assignments", "description": "Create, assign and manage assignments", "url": "faculty_assignments"},
        {"title": "Review Submissions", "description": "View pending and completed submissions", "url": "faculty_review_submissions"},
        {"title": "Student Stats", "description": "Ranks of students in class, dept, and CodeBuzz", "url": "faculty_student_stats"},
        {"title": "Leaderboard", "description": "Top performing students", "url": "faculty_leaderboard"},
        {"title": "Class Test", "description": "Create and manage tests", "url": "faculty_class_test"},
        {"title": "Technical Contests", "description": "Manage coding contests", "url": "faculty_contests"},
        {"title": "Problem Bank", "description": "Add or manage coding problems", "url": "faculty_problem_bank"},
        {"title": "Notifications & Announcements", "description": "Send important announcements", "url": "faculty_notifications"},
        {"title": "My Profile", "description": "Edit your profile settings", "url": "faculty_profile"},
    ]

    context = {
        "total_students": 48,
        "total_problems": 21,
        "pending_reviews": 14,
        "total_contests": 3,
        "features": features,
        'faculty': faculty,
    }

    return render(request, 'faculty/faculty_dashboard.html', context)


def faculty_profile(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')  # Redirect to login if not authenticated

    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty/faculty_profile.html', {'faculty': faculty})

@login_required
def faculty_my_class(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty/faculty_my_class.html', {'faculty': faculty})

@login_required
def faculty_problems(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty/faculty_problems.html', {'faculty': faculty})

@login_required
def faculty_assignments(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty/faculty_assignments.html', {'faculty': faculty})

@login_required
def faculty_review_submissions(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty/faculty_review_submissions.html', {'faculty': faculty})

@login_required
def faculty_student_stats(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty/faculty_student_stats.html', {'faculty': faculty})

@login_required
def faculty_leaderboard(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty/faculty_leaderboard.html', {'faculty': faculty})

@login_required
def faculty_class_test(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty/faculty_class_test.html', {'faculty': faculty})

@login_required
def faculty_contests(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty/faculty_contests.html', {'faculty': faculty})

@login_required
def faculty_problem_bank(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty/faculty_problem_bank.html', {'faculty': faculty})

@login_required
def faculty_profile(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty/faculty_profile.html', {'faculty': faculty})

@login_required
def faculty_notifications(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty/faculty_notifications.html', {'faculty': faculty})

def faculty_logout(request):
    request.session.flush()
    return redirect('home')

# Create admin views here.

def admin_dashboard(request):
    admin_id = request.session.get('admin_id')
    
    if not admin_id:
        return redirect('login')
    try:
        admin = Admin.objects.get(id=admin_id)
    except Admin.DoesNotExist:
        # If admin with the given ID is not found, redirect to login
        return redirect('login')
    
    
    context = {
        "hod_name": "Dr. Divvya Yadav",
        "total_faculty": 68,
        "total_students": 1720,
        "active_problems": 45,
        "top_performer": "Aryan Kumar (CS-3B)",
        'admin': admin,
        }
    return render(request, 'admin/admin_dashboard.html', context)

def admin_profile(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')  # Redirect to login if not authenticated

    try:
        admin = Admin.objects.get(id=admin_id)
    except Admin.DoesNotExist:
        return redirect('login')

    return render(request, 'admin/admin_profile.html', {'admin': admin})

def admin_logout(request):
    request.session.flush()
    return redirect('home')