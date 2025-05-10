from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('create_company/', views.create_company, name='create_company'),
    path('<int:pk>/', views.company_detail, name='company_detail'),
    path('<int:pk>/edit_company/', views.update_company, name='update_company'),
    path('<int:pk>/delete_company/', views.delete_company, name='delete_company'),
]
