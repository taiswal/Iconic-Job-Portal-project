from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_to_job, name='apply_to_job'),
    path('bookmark/<int:job_id>/', views.bookmark_job, name='bookmark_job'),
]
