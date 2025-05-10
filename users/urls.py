
from django.urls import path
from .views import register,logout,redirect_after_login

urlpatterns = [
    # path('register/', register, name='register'),
    # path('login/', user_login, name='user_login'),
    path('logout/', logout, name='logout'),
    path('redirect-after-login/', redirect_after_login, name='redirect_after_login'),
]