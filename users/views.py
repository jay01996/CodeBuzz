from django.shortcuts import render

# Create your views here.
def user_login(request):
    return render(request, 'login.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')