from django.shortcuts import *
from accounts.models import Admin, Student, Faculty
from django.contrib.auth.decorators import login_required

# Create your views here.
def manage_students(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    admin = Admin.objects.get(id=admin_id)
    students = Student.objects.all()  # Add filters if needed
    
    context = {
        'admin': admin,
        'students': students
    }
    return render(request, 'manage_students.html', context)

def manage_faculty(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    admin = Admin.objects.get(id=admin_id)

    context = {
        'admin': admin
    }
     
    if request.method == "POST":
        # Handle form submission here
        pass

    return render(request, 'manage_faculty.html', context)


def manage_problem(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    admin = Admin.objects.get(id=admin_id)

    if request.method == "POST":
        # Handle problem creation
        pass

    return render(request, 'manage_problem.html', {'admin': admin})

def display_ranking(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    admin = Admin.objects.get(id=admin_id)

    rankings = [45]  # Replace with logic to calculate department ranking
    return render(request, 'display_ranking.html', {'rankings': rankings, 'admin': admin})

def view_reports(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    admin = Admin.objects.get(id=admin_id)

    reports = []  # List of generated reports or a download button
    return render(request, 'view_reports.html', {'reports': reports, 'admin': admin})


def manage_syllabus(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    admin = Admin.objects.get(id=admin_id)

    if request.method == "POST":
        # Handle file upload and form save
        pass

    return render(request, 'manage_syllabus.html', {'admin': admin})

def create_announcement(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    admin = Admin.objects.get(id=admin_id)

    if request.method == "POST":
        # Save announcement to DB
        pass

    return render(request, 'create_announcement.html', {'admin': admin})

def email_students(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    admin = Admin.objects.get(id=admin_id)

    if request.method == "POST":
        # Send email logic
        pass

    return render(request, 'email_students.html', {'admin': admin})


def student_logs(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    admin = Admin.objects.get(id=admin_id)

    logs = []  # Fetch from logs model or table
    return render(request, 'student_logs.html', {'logs': logs, 'admin': admin})

def update_student(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    admin = Admin.objects.get(id=admin_id)

    return render(request, 'update_student.html', {'admin': admin})

