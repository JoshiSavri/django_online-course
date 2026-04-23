from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),

<<<<<<< HEAD
    path('submit/<int:course_id>/', views.submit_exam, name='submit_exam'),

    path('result/<int:submission_id>/', views.show_exam_result, name='show_exam_result'),
]
=======
    # ✅ REQUIRED
    path('submit/<int:course_id>/', views.submit_exam, name='submit_exam'),

    # ✅ REQUIRED
    path('result/<int:submission_id>/', views.show_exam_result, name='show_exam_result'),
]
>>>>>>> fe9c786a3fb822416ddb4d3dfb3bf7ae22e5f485
