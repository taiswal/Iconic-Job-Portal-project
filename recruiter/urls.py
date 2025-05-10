from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_recruiter_profile, name='create_recruiter_profile'),
    path('update/', views.update_recruiter_profile, name='update_recruiter_profile'),
    path('delete/', views.delete_recruiter_profile, name='delete_recruiter_profile'),
    path('view/', views.view_recruiter_profile, name='view_recruiter_profile'),
]
