from posts.models import UserProfile
from posts.models import Tag
from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from posts.models import Post, Tag
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.



# --------- Create Views --------- #

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Post created successfully.")
            return redirect('list_posts')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})
# def create_post(request):
#     """
#     Create a new blog post with title, content, user, tags, and optional image.
    
#     This view handles both GET and POST requests:
#     - GET: Displays the create post form with user and tag options
#     - POST: Processes the submitted form data to create a new post
    
#     The function collects form data including title, content, user selection,
#     multiple tag selections, and an optional image upload.
#     """
#     if request.method == 'POST':
#         # Extract form data from the POST request
#         title = request.POST.get('title')  # Get the post title
#         content = request.POST.get('content')  # Get the post content
#         user_id = request.POST.get('user')  # Get the selected user ID
#         tag_ids = request.POST.getlist('tags')  # Get multiple selected tag IDs
#         image = request.FILES.get('image')  # Get uploaded image if any

#         # Retrieve the user object based on the selected user ID
#         user = User.objects.get(id=user_id)
        
#         # Create a new post with the collected data
#         post = Post.objects.create(
#             user=user, title=title, content=content, image=image)
        
#         # If tags were selected, associate them with the post
#         if tag_ids:
#             post.tags.set(tag_ids)  # Set many-to-many relationship with tags
            
#         post.save()  # Save the post to the database
#         return redirect('list_posts')  # Redirect to the posts listing page

#     # For GET requests, prepare data for the form
#     users = User.objects.all()  # Get all users for the dropdown
#     tags = Tag.objects.all()  # Get all tags for the multi-select
#     return render(request, 'posts/create_post.html', {'users': users, 'tags': tags})


def create_tag(request):
    """
    Create a new tag with a name.
    
    This view handles both GET and POST requests:
    - GET: Displays the create tag form
    - POST: Processes the submitted form data to create a new tag
    
    The function collects form data including tag name.
    """
    
    # Handle POST request to create a new tag
    if request.method == 'POST':
        # Extract tag name from the POST request
        tag_name = request.POST.get('tag_name') 
        
        # Create a new tag with the collected data
        Tag.objects.create(tag_name=tag_name)
        
        # Redirect to the tags listing page
        return redirect('list_tags')
    
    return render(request, 'posts/create_tag.html')


def create_user(request):
    """
    Create a new user with name, email, phone, and password.
    
    This view handles both GET and POST requests:
    - GET: Displays the create user form
    - POST: Processes the submitted form data to create a new user

    The function collects form data including name, email, phone, and password.
    """
    if request.method == 'POST':
        # Extract form data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        user = User.objects.create_user(
            email=email, name=name, password=password, phone=phone)
        return redirect('list_posts')
    return render(request, 'posts/create_user.html')


def create_user_profile(request):
    """
    Create a new user profile with bio and profile picture.
    
    This view handles both GET and POST requests:
    - GET: Displays the create user profile form
    - POST: Processes the submitted form data to create a new user profile
    
    The function collects form data including user selection, bio, and profile picture.
    """
    if request.method == 'POST':
        # Extract form data from the POST request
        user_id = request.POST.get('user')
        bio = request.POST.get('bio')
        profile_picture = request.FILES.get('profile_picture')

        # Retrieve the user object based on the selected user ID
        user = User.objects.get(id=user_id)
        
        # Create a new user profile with the collected data
        UserProfile.objects.create(
            user=user, bio=bio, profile_picture=profile_picture)
        return redirect('list_posts')

    users = User.objects.all()  # Get all users for the dropdown
    return render(request, 'posts/create_user_profile.html', {'users': users})


def list_posts(request):
    """
    List all blog posts.
    
    This view handles GET requests to display a list of all blog posts.
    
    """
    posts = Post.objects.all()  # Get all posts from the database
    return render(request, 'posts/list_posts.html', {'posts': posts})

def list_tags(request):
    tags = Tag.objects.all()
    return render(request, 'posts/list_tags.html', {'tags': tags})

def list_users(request):
    users = User.objects.all()
    return render(request, 'posts/list_users.html', {'users': users})

def list_user_profiles(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'posts/list_user_profiles.html', {'user_profiles': user_profiles})


def update_post(request, post_id):
    """
    Update an existing blog post with title, content, user, tags, and optional image.
    
    This view handles both GET and POST requests:
    - GET: Displays the update post form with current post data
    - POST: Processes the submitted form data to update the post
    
    The function collects form data including title, content, user selection,
    multiple tag selections, and an optional image upload.
    Only the owner of the post can update it. 
    """
    
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:
        messages.error(request, "You don't have permission to update this post.")
        return redirect('list_posts')
    if request.method == 'POST':
        # Extract form data from the POST request
        title = request.POST.get('title')
        content = request.POST.get('content')
        user_id = request.POST.get('user')
        tag_ids = request.POST.getlist('tags')
        image = request.FILES.get('image')

        # Update the post with the collected data
        post.image = image
        post.user = User.objects.get(id=user_id)
        post.title = title
        post.content = content
        post.save()  # Save the updated post to the database
        post.tags.set(tag_ids)  # Set many-to-many relationship with tags
        
        # Redirect to the posts listing page
        return redirect('list_posts')
    
    # For GET requests, prepare data for the form
    users = User.objects.all()  # Get all users for the dropdown
    tags = Tag.objects.all()  # Get all tags for the multi-select
    return render(request, 'posts/update_post.html', {'post': post, 'users': users, 'tags': tags})


def update_tag(request, tag_id):
    """
    Update an existing tag with a name.
    
    This view handles both GET and POST requests:
    - GET: Displays the update tag form with current tag data
    - POST: Processes the submitted form data to update the tag
    
    The function collects form data including tag name.
    """
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == 'POST':
        # Extract form data from the POST request
        tag_name = request.POST.get('tag_name')
        
        # Update the tag with the collected data
        tag.tag_name = tag_name
        tag.save()  # Save the updated tag to the database
        
        # Redirect to the tags listing page
        return redirect('list_tags')
    
    return render(request, 'posts/update_tag.html', {'tag': tag})


def update_user(request, user_id):
    """
    Update an existing user with name, email, phone, and password.
    
    This view handles both GET and POST requests:
    - GET: Displays the update user form with current user data
    - POST: Processes the submitted form data to update the user

    The function collects form data including name, email, phone, and password.
    """
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        # Extract form data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        # Update the user with the collected data
        user.name = name
        user.email = email
        user.phone = phone
        if password:
            user.set_password(password)
        user.save()  # Save the updated user to the database
        
        # Redirect to the users listing page
        return redirect('list_users')
    
    return render(request, 'posts/update_user.html', {'user': user})


def update_user_profile(request, user_profile_id):
    """
    Update an existing user profile with bio and profile picture.
    
    This view handles both GET and POST requests:
    - GET: Displays the update user profile form with current user profile data
    - POST: Processes the submitted form data to update the user profile

    The function collects form data including user selection, bio, and profile picture.
    """
    user_profile = get_object_or_404(UserProfile, id=user_profile_id)
    if request.method == 'POST':
        # Extract form data from the POST request
        user_id = request.POST.get('user')
        bio = request.POST.get('bio')
        profile_picture = request.FILES.get('profile_picture')

        # Update the user profile with the collected data
        user_profile.user = User.objects.get(id=user_id)
        user_profile.bio = bio
        user_profile.profile_picture = profile_picture
        user_profile.save()  # Save the updated user profile to the database
        
        # Redirect to the user profiles listing page
        return redirect('list_user_profiles')
    
    # For GET requests, prepare data for the form
    users = User.objects.all()  # Get all users for the dropdown
    return render(request, 'posts/update_user_profile.html', {'user_profile': user_profile, 'users': users})

def delete_post(request, post_id):
    """
    Delete an existing blog post.
    
    This view handles GET requests to delete a blog post.
    Only the owner of the post can delete it.
    """
    post = get_object_or_404(Post, id=post_id)
    
    # Check if the current user is the owner of the post
    if request.user != post.user:
        messages.error(request, "You don't have permission to delete this post.")
        return redirect('list_posts')
    
    post.delete()
    messages.success(request, "Post deleted successfully.")
    return redirect('list_posts')

def delete_tag(request, tag_id):
    """
    Only the owner of the tag can delete it.
    Delete an existing tag.
    
    This view handles GET requests to delete a tag.
    """
    tag = get_object_or_404(Tag, id=tag_id)
    if request.user != tag.user:
        messages.error(request, "You don't have permission to delete this tag.")
        return redirect('list_tags')
    
    tag.delete()
    messages.success(request, "Tag deleted successfully.")
    return redirect('list_tags')

# def delete_user(request, user_id):
#     """
#     Only the owner of the user can delete it.
#     Delete an existing user.
    
#     This view handles GET requests to delete a user.
#     """
#     user = get_object_or_404(User, id=user_id)
#     if request.user != user:
#         messages.error(request, "You don't have permission to delete this user.")
#         return redirect('list_users')
#     else:
#         user.delete()
#         messages.success(request, "User deleted successfully.")
#         return redirect('list_users')
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.user != user and not request.user.is_superuser:
        messages.error(request, "You don't have permission to delete this user.")
        return redirect('list_users')

    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully.")
        return redirect('list_users')

    return render(request, 'posts/confirm_delete_user.html', {'user': user})


def delete_user_profile(request, user_profile_id):
    """
    Only the owner of the user profile can delete it.
    Delete an existing user profile.
    
    This view handles GET requests to delete a user profile.
    """
    user_profile = get_object_or_404(UserProfile, id=user_profile_id)
    if request.user != user_profile.user:
        messages.error(request, "You don't have permission to delete this user profile.")
        return redirect('list_user_profiles')
    
    user_profile.delete()
    messages.success(request, "User profile deleted successfully.")
    return redirect('list_user_profiles')


