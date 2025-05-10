from django.contrib import admin
from django.urls import path,include
from .views import *
# from . import views

urlpatterns = [
    # path('index/',views.index,name='index'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    path('index/',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    
]
 