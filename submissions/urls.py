from django.urls import path
from .views import *

urlpatterns = [
    path('practice/', practice_home, name='practice_home'),
    path('todays-problem/', todays_problem, name='todays_problem'),
    path('solved-problems/', solved_problems, name='solved_problems'),
    path('pending-problems/', pending_problems, name='pending_problems'),
    path('practice-problems/', practice_problems, name='practice_problems'),
     path('leaderboard/', leaderboard, name='leaderboard'),
]
