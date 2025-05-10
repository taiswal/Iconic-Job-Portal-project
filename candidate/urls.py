from django.urls import path
from . import views

urlpatterns = [
    path('candidate/create/', views.create_candidate_profile, name='create_candidate_profile'),
    path('candidate/', views.view_candidate_profile, name='view_candidate_profile'),
    path('candidate/update/', views.update_candidate_profile, name='update_candidate_profile'),
    path('candidate/delete/', views.delete_candidate_profile, name='delete_candidate_profile'),
]
