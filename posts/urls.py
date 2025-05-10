
from django.urls import path
from . import views
from posts.views import create_post

urlpatterns = [

    # Job Post URLs
    path('create_post/', create_post, name='create_post'),
    path('list_posts/', views.list_posts, name='list_posts'),
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),

    # Tag URLs
    path('create_tag/', views.create_tag, name='create_tag'),
    path('list_tags/', views.list_tags, name='list_tags'),
    path('update_tag/<int:tag_id>/', views.update_tag, name='update_tag'),
    path('delete_tag/<int:tag_id>/', views.delete_tag, name='delete_tag'),

    # User URLs
    path('create_user/', views.create_user, name='create_user'),
    path('list_users/', views.list_users, name='list_users'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

     # User Profile URLs
    path('create_user_profile/', views.create_user_profile, name='create_user_profile'),
    path('list_user_profiles/', views.list_user_profiles, name='list_user_profiles'),
    path('update_user_profile/<int:user_profile_id>/', views.update_user_profile, name='update_user_profile'),
    path('delete_user_profile/<int:user_profile_id>/', views.delete_user_profile, name='delete_user_profile'),
    
]



   

   
