from django.urls import path
from . import views
from job.views import home
from users.views import user_login,register

urlpatterns = [
    path('',home,name='home'),
    path('login/', user_login, name='user_login'),
    path('register/', register, name='register'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('my-bookmarks/', views.my_bookmarks, name='my_bookmarks'),
    path('job/<int:job_id>/applications/', views.job_applications, name='job_applications'),
    path('application/<int:app_id>/status/<str:status>/', views.update_application_status, name='update_application_status'),
    path('dashboard/candidate/', views.candidate_dashboard, name='candidate_dashboard'),
    path('dashboard/recruiter/', views.recruiter_dashboard, name='recruiter_dashboard'),
]
