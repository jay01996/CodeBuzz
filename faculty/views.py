from django.shortcuts import render,redirect
from faculty.models import Faculty



# Create your views here.
def faculty_dashboard(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')
    faculty = Faculty.objects.get(id=faculty_id)
    return render(request, 'faculty_dashboard.html', {'faculty': faculty})


def faculty_profile(request):
    faculty_id = request.session.get('faculty_id')
    if not faculty_id:
        return redirect('login')  # Redirect to login if not authenticated

    try:
        faculty = Faculty.objects.get(id=faculty_id)
    except Faculty.DoesNotExist:
        return redirect('login')

    return render(request, 'faculty_profile.html', {'faculty': faculty})
