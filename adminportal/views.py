from django.shortcuts import *
from accounts.models import Admin, Student, Faculty
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from institute.models import Course, Branch, Semester, Section, Group, Department
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib import messages
from .forms import StudentUpdateForm
from django.db import IntegrityError
from .models import *

def manage_students(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    
    try:
        admin = Admin.objects.get(id=admin_id)
    except Admin.DoesNotExist:
        return redirect('login')

    # Get all students first
    students = Student.objects.all()

    # Search filter
    query = request.GET.get('q', '').strip()
    if query:
        students = students.filter(
            Q(student_id__icontains=query) |
            Q(roll_no__icontains=query) |
            Q(email__icontains=query)
        )

    # Dynamic dropdown filters
    filter_fields = ['course', 'branch', 'semester', 'section', 'group']
    for field in filter_fields:
        value = request.GET.get(field)
        if value:
            students = students.filter(**{f"{field}_id": value})

    students = students.order_by('id')

    context = {
        'students': students,
        'courses': Course.objects.all(),
        'branches': Branch.objects.all(),
        'semesters': Semester.objects.all(),
        'sections': Section.objects.all(),
        'groups': Group.objects.all(),
         'admin': admin,
    }

    return render(request, 'manage_students.html', context)

def load_branches(request):
    course_id = request.GET.get('course_id')
    branches = Branch.objects.filter(course_id=course_id).values('id', 'name')
    return JsonResponse(list(branches), safe=False)

def load_semesters(request):
    branch_id = request.GET.get('branch_id')
    semesters = Semester.objects.filter(branch_id=branch_id).values('id', 'number')
    return JsonResponse(list(semesters), safe=False)

def load_sections(request):
    semester_id = request.GET.get('semester_id')
    sections = Section.objects.filter(semester_id=semester_id).values('id', 'name')
    return JsonResponse(list(sections), safe=False)

def load_groups(request):
    section_id = request.GET.get('section_id')
    groups = Group.objects.filter(section_id=section_id).values('id', 'name')
    return JsonResponse(list(groups), safe=False)


def manage_faculty(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')
    admin = Admin.objects.get(id=admin_id)
    faculty_list = Faculty.objects.select_related('department').all().order_by('id')

    context = {
        'admin': admin,
        'faculty_list': faculty_list,
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


# def manage_syllabus(request):
#     admin_id = request.session.get('admin_id')
#     if not admin_id:
#         return redirect('login')
#     admin = Admin.objects.get(id=admin_id)

#     if request.method == "POST":
#         # Handle file upload and form save
#         pass

#     return render(request, 'manage_syllabus.html', {'admin': admin})

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


def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student details updated successfully.')
            return redirect('manage_students')  # replace with your actual list view
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentUpdateForm(instance=student)

    return render(request, 'update_student.html', {'form': form, 'student': student})

# def update_faculty(request, cbf_id):
#     faculty = get_object_or_404(Faculty, pk=cbf_id)

#     if request.method == 'POST':
#         form = FacultyUpdateForm(request.POST, request.FILES, instance=faculty)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Faculty details updated successfully.')
#             return redirect('manage_faculty')  # replace with your actual list view
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = FacultyUpdateForm(instance=faculty)

#     return render(request, 'update_faculty.html', {'form': form, 'faculty': faculty})   

def update_faculty(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    departments = Department.objects.all()

    if request.method == 'POST':
        faculty.full_name = request.POST.get('full_name')
        faculty.employee_id = request.POST.get('employee_id')
        faculty.department_id = request.POST.get('department')
        faculty.email = request.POST.get('email')
        faculty.contact_number = request.POST.get('contact_number')
        faculty.gender = request.POST.get('gender')
        faculty.dob = request.POST.get('dob')
        faculty.address = request.POST.get('address')

        if request.FILES.get('profile_photo'):
            faculty.profile_photo = request.FILES.get('profile_photo')

        faculty.save()
        messages.success(request, 'Faculty details updated successfully.')
        return redirect('manage_faculty')

    context = {
        'faculty': faculty,
        'departments': departments
    }
    return render(request, 'update_faculty.html', context)


def delete_faculty(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    faculty.delete()
    messages.success(request, 'Faculty deleted successfully.')
    return redirect('manage_faculty')



def add_faculty(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login')

    try:
        admin = Admin.objects.select_related('department', 'college', 'university').get(id=admin_id)
    except Admin.DoesNotExist:
        messages.error(request, "Unauthorized access.")
        return redirect('login')

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        employee_id = request.POST.get('employee_id')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        profile_photo = request.FILES.get('profile_photo')

        # Check for duplicate employee_id or email
        if Faculty.objects.filter(employee_id=employee_id).exists():
            messages.error(request, 'Employee ID already exists.')
            return redirect('add_faculty')

        if Faculty.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('add_faculty')

        try:
            faculty = Faculty(
                full_name=full_name,
                employee_id=employee_id,
                email=email,
                contact_number=contact_number,
                gender=gender,
                dob=dob,
                address=address,
                profile_photo=profile_photo,
                department=admin.department,
                college=admin.college,
                university=admin.university
            )
            faculty.save()  # CBF ID generated automatically
            messages.success(request, 'Faculty added successfully.')
            return redirect('manage_faculty')

        except IntegrityError:
            messages.error(request, 'An error occurred while saving. Please try again.')

    context = {
        'university': admin.university,
        'college': admin.college,
        'department': admin.department,
    }
    return render(request, 'add_faculty.html', context)


def admin_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('admin_id'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

@admin_login_required
def manage_subjects(request):
    editing = False
    subject = None

    if 'edit' in request.GET:
        subject = get_object_or_404(Subject, id=request.GET['edit'])
        editing = True

        if request.method == 'POST':
            form_data = request.POST
            subject.subject_code = form_data.get('subject_code')
            subject.subject_name = form_data.get('subject_name')
            subject.subject_type = form_data.get('subject_type')
            subject.credits = form_data.get('credits')
            subject.department_id = form_data.get('department')
            subject.course_id = form_data.get('course')
            subject.branch_id = form_data.get('branch')
            subject.semester_id = form_data.get('semester')
            subject.save()
            messages.success(request, "Subject updated successfully.")
            return redirect('manage_subjects')  # replace with your URL name

    elif request.method == 'POST':
        # Handle subject creation
        Subject.objects.create(
            subject_code=request.POST['subject_code'],
            subject_name=request.POST['subject_name'],
            subject_type=request.POST['subject_type'],
            credits=request.POST['credits'],
            department_id=request.POST['department'],
            course_id=request.POST['course'],
            branch_id=request.POST['branch'],
            semester_id=request.POST['semester']
        )
        messages.success(request, "Subject added successfully.")
        return redirect('manage_subjects')

    context = {
        'departments': Department.objects.all(),
        'courses': Course.objects.all(),
        'branches': Branch.objects.all(),
        'semesters': Semester.objects.all(),
        'subjects': Subject.objects.all(),
        'editing': editing,
        'subject': subject,
    }
    return render(request, 'manage_subjects.html', context)


def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    subject.delete()
    messages.success(request, "Subject deleted successfully.")
    return redirect('manage_subjects')

# syllabus/views.py

@admin_login_required
def manage_syllabus(request):
    subjects = Subject.objects.all()
    syllabus_entries = Syllabus.objects.select_related('subject').all()

    # Handle POST request (Add or Update syllabus)
    if request.method == 'POST':
        subject_id = request.POST.get('subject')
        subject = get_object_or_404(Subject, id=subject_id)

        program_number = request.POST.get('program_number')
        program_title = request.POST.get('program_title')
        program_description = request.POST.get('program_description')
        difficulty_level = request.POST.get('difficulty_level')
        marks = request.POST.get('marks')

        syllabus_id = request.POST.get('syllabus_id')
        if syllabus_id:
            # Update existing syllabus entry
            syllabus = get_object_or_404(Syllabus, id=syllabus_id)
            syllabus.subject = subject
            syllabus.program_number = program_number
            syllabus.program_title = program_title
            syllabus.program_description = program_description
            syllabus.difficulty_level = difficulty_level
            syllabus.marks = marks
            syllabus.save()
            messages.success(request, "Syllabus program updated successfully.")
        else:
            # Create new syllabus entry
            Syllabus.objects.create(
                subject=subject,
                program_number=program_number,
                program_title=program_title,
                program_description=program_description,
                difficulty_level=difficulty_level,
                marks=marks,
                added_by=request.user
            )
            messages.success(request, "Syllabus program added successfully.")

        return redirect('manage_syllabus')

    # Edit mode
    editing = None
    edit_id = request.GET.get('edit')
    if edit_id:
        editing = get_object_or_404(Syllabus, id=edit_id)

    difficulty_levels = ['Easy', 'Medium', 'Hard']

    return render(request, 'manage_syllabus.html', {
        'subjects': subjects,
        'syllabus_entries': syllabus_entries,
        'editing': editing,
        'difficulty_levels': difficulty_levels,
    })
    
    
@admin_login_required
def delete_syllabus(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, id=syllabus_id)
    
    # Optional: check if the logged-in user has permission
    if request.user != syllabus.added_by and not request.user.is_superuser:
        messages.error(request, "You are not authorized to delete this entry.")
        return redirect('manage_syllabus')

    syllabus.delete()
    messages.success(request, "Syllabus entry deleted successfully.")
    return redirect('manage_syllabus')  # Make sure this name matches your manage view URL



# views.py



@admin_login_required
def manage_faculty_assignments(request):
    # Get current logged-in admin object
    admin_id = request.session.get('admin_id')
    if not admin_id:
        messages.error(request, "Admin not logged in.")
        return redirect('admin_login')

    admin = get_object_or_404(Admin, id=admin_id)
    department = admin.department

    subjects = Subject.objects.filter(department=department)
    faculties = Faculty.objects.filter(department=department)
    branches = Branch.objects.all()
    semesters = Semester.objects.all()
    sections = Section.objects.all()
    courses = Course.objects.all()
    groups = Group.objects.all()

    editing = False
    assignment = None
    
    # ✅ Handle delete
    if request.GET.get('delete'):
        assignment = get_object_or_404(FacultySubjectAssignment, id=request.GET.get('delete'))
        assignment.delete()
        messages.success(request, "Assignment deleted successfully.")
        return redirect("manage_faculty_assignments")

    if request.method == "POST":
        subject_id = request.POST['subject']
        faculty_id = request.POST['faculty']
        branch_id = request.POST['branch']
        semester_id = request.POST['semester']
        section_id = request.POST['section']
        course_id = request.POST['course']
        group_id = request.POST.get('group')

        if request.GET.get('edit'):
            assignment = get_object_or_404(FacultySubjectAssignment, id=request.GET.get('edit'))
        else:
            assignment = FacultySubjectAssignment()

        assignment.subject_id = subject_id
        assignment.faculty_id = faculty_id
        assignment.branch_id = branch_id
        assignment.semester_id = semester_id
        assignment.section_id = section_id
        assignment.course_id = course_id
        assignment.group_id = group_id if group_id else None
        assignment.assigned_by = admin
        assignment.save()

        messages.success(request, "Assignment saved successfully.")
        return redirect("manage_faculty_assignments")

    if request.GET.get('edit'):
        editing = True
        assignment = get_object_or_404(FacultySubjectAssignment, id=request.GET.get('edit'))

    assignments = FacultySubjectAssignment.objects.filter(subject__department=department)

    return render(request, "manage_faculty_assignments.html", {
        "editing": editing,
        "assignment": assignment,
        "subjects": subjects,
        "faculties": faculties,
        "branches": branches,
        "semesters": semesters,
        "sections": sections,
        "courses": courses,
        "groups": groups,
        "assignments": assignments
    })
