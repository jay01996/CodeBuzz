from django.shortcuts import render

# Create your views here.
from django.shortcuts import *
from django.db.models import *
from accounts.models import Student 
from datetime import date, timedelta
from .models import *

def todays_problem(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')

    today = date.today()
    problems = Problem.objects.filter(
        assigned_to__id=student_id,
        assigned_date__lte=today,
        assigned_date__gte=today - timedelta(days=3)
    )

    return render(request, 'todays_problem.html', {'problems': problems})
# adjust if student model is elsewhere

# Practice Home Page with Tabs
def practice_home(request):
    return render(request, 'practice.html')

# Today's Problem
# def todays_problem(request):
#     # problem = Problem.objects.filter(is_today=True).first()  # assuming you have a boolean field
#     # return render(request, 'todays_problem.html', {'problem': problem})
#     return render(request, 'todays_problem.html')




# Solved Problems
# def solved_problems(request):
#     # student_id = request.session.get('student_id')
#     # problems = Submission.objects.filter(student_id=student_id, status='solved').select_related('problem')
#     # return render(request, 'solved_problems.html', {'problems': problems})
#     return render(request, 'solved_problems.html')

def solved_problems(request):
    # student_id = request.session.get('student_id')
    # if not student_id:
    #     return redirect('login')

    # solved = Submission.objects.filter(student__id=student_id, is_correct=True).select_related('problem')

    return render(request, 'solved_problems.html')

# Pending Problems
# def pending_problems(request):
#     # student_id = request.session.get('student_id')
#     # problems = Submission.objects.filter(student_id=student_id, status='pending').select_related('problem')
#     # return render(request, 'pending_problems.html', {'problems': problems})
#     return render(request, 'pending_problems.html')

def pending_problems(request):
    # student_id = request.session.get('student_id')
    # if not student_id:
    #     return redirect('login')

    # solved_ids = Submission.objects.filter(student__id=student_id, is_correct=True).values_list('problem_id', flat=True)
    # pending = Problem.objects.filter(assigned_to__id=student_id).exclude(id__in=solved_ids)

    return render(request, 'pending_problems.html')


# Practice Problems (all problems)
# def practice_problems(request):
#     # problems = Problem.objects.all()
#     # return render(request, 'practice_problems.html', {'problems': problems})
#     return render(request, 'practice_problems.html')

from .models import PracticeProblem

def practice_problems(request):
    problems = PracticeProblem.objects.all()
    return render(request, 'practice_problems.html', {'problems': problems})

def leaderboard(request):
    # Get filter values from query params
    university = request.GET.get('university')
    college = request.GET.get('college')
    branch = request.GET.get('branch')
    semester = request.GET.get('semester')

    # Filter query
    filters = Q()
    if university:
        filters &= Q(university=university)
    if college:
        filters &= Q(college=college)
    if branch:
        filters &= Q(branch=branch)
    if semester:
        filters &= Q(semester=semester)

    # Leaderboard data
    leaderboard_data = (
        Student.objects.filter(filters)
        .annotate(
            total_score=Sum('submission__score'),
            problems_solved=Count('submission', filter=Q(submission__is_correct=True)),
            last_submission=Max('submission__submitted_at')
        )
        .order_by('-total_score', '-problems_solved')
    )

    # Get unique values for dropdowns
    universities = Student.objects.values_list('university', flat=True).distinct().order_by('university')
    colleges = Student.objects.values_list('college', flat=True).distinct().order_by('college')
    branches = Student.objects.values_list('branch', flat=True).distinct().order_by('branch')
    semesters = Student.objects.values_list('semester', flat=True).distinct().order_by('semester')

    context = {
        'leaderboard': leaderboard_data,
        'filters': {
            'university': university,
            'college': college,
            'branch': branch,
            'semester': semester,
        },
        'universities': universities,
        'colleges': colleges,
        'branches': branches,
        'semesters': semesters,
    }
    return render(request, 'leaderboard.html', context)
   