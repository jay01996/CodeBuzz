from django.shortcuts import *
from .models import RankRecord
from accounts.models import Student

# Practice Home Page with Tabs
def rank(request):
    return render(request, 'rank.html')

def class_rank(request):
    student = Student.objects.get(id=request.session['student_id'])
    ranks = RankRecord.objects.filter(
        student__branch=student.branch,
        student__semester=student.semester,
        student__section=student.section
    )
    return render(request, 'class_rank.html', {'ranks': ranks})

def college_rank(request):
    student = Student.objects.get(id=request.session['student_id'])
    ranks = RankRecord.objects.filter(
        student__college=student.college
    )
    return render(request, 'college_rank.html', {'ranks': ranks})

def department_rank(request):
    student = Student.objects.get(id=request.session['student_id'])
    ranks = RankRecord.objects.filter(
        student__department=student.department
    )
    return render(request, 'department_rank.html', {'ranks': ranks})

def codebuzz_rank(request):
    ranks = RankRecord.objects.all()
    return render(request, 'codebuzz_rank.html', {'ranks': ranks})
