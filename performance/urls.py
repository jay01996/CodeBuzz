from django.urls import path
from .views import *

urlpatterns = [
    path('rank/', rank, name='rank'),
    path('class-rank/', class_rank, name='class_rank'),
    path('college-rank/', college_rank, name='college_rank'),
    path('department-rank/', department_rank, name='department_rank'),
    path('codebuzz-rank/', codebuzz_rank, name='codebuzz_rank'),
]
