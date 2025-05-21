from django.shortcuts import *
from .models import Syllabus
from users.models import Student

def syllabus_view(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')

    student = Student.objects.get(id=student_id)
    syllabus_list = Syllabus.objects.filter(
        course=student.course,
        semester=student.semester,
        branch=student.branch,
        department=student.department
    )

    context = {
        'syllabus_list': syllabus_list,
        'student': student
    }
    return render(request, 'syllabus.html', context)
