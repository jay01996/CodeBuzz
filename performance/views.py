from django.shortcuts import render
from users.models import Student  # adjust if student model is elsewhere

# Practice Home Page with Tabs
def rank(request):
    return render(request, 'rank.html')

# class_rank
def class_rank(request):
    return render(request, 'class_rank.html')


# codebuzz_rank
def codebuzz_rank(request):
    return render(request, 'codebuzz_rank.html')

# department_rank
def department_rank(request):
    return render(request, 'department_rank.html')

# college_rank
def college_rank(request):
    return render(request, 'college_rank.html')
