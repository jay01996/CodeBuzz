from django.shortcuts import render
# from .models import Problem, Submission
from users.models import Student  # adjust if student model is elsewhere

# Practice Home Page with Tabs
def practice_home(request):
    return render(request, 'practice.html')

# Today's Problem
def todays_problem(request):
    # problem = Problem.objects.filter(is_today=True).first()  # assuming you have a boolean field
    # return render(request, 'todays_problem.html', {'problem': problem})
    return render(request, 'todays_problem.html')


# Solved Problems
def solved_problems(request):
    # student_id = request.session.get('student_id')
    # problems = Submission.objects.filter(student_id=student_id, status='solved').select_related('problem')
    # return render(request, 'solved_problems.html', {'problems': problems})
    return render(request, 'solved_problems.html')

# Pending Problems
def pending_problems(request):
    # student_id = request.session.get('student_id')
    # problems = Submission.objects.filter(student_id=student_id, status='pending').select_related('problem')
    # return render(request, 'pending_problems.html', {'problems': problems})
    return render(request, 'pending_problems.html')

# Practice Problems (all problems)
def practice_problems(request):
    # problems = Problem.objects.all()
    # return render(request, 'practice_problems.html', {'problems': problems})
    return render(request, 'practice_problems.html')
