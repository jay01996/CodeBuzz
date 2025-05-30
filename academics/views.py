from django.shortcuts import *
from .models import Syllabus
from accounts.models import Student

def syllabus_view(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')

    student = get_object_or_404(Student, id=student_id)

    # Use the actual IDs for filtering – not full objects
    syllabus_list = Syllabus.objects.filter(
        course_id=student.course_id,
        semester_id=student.semester_id,
        branch_id=student.branch_id,
        department_id=student.department_id
    )

    context = {
        'syllabus_list': syllabus_list,
        'student': student
    }
    return render(request, 'syllabus.html', context)
