from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Custom manager to handle user creation
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, name, password, **extra_fields)


# Custom user model for job portal
class User(AbstractBaseUser, PermissionsMixin):
    # Common fields
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    USER_TYPES = (
        ('candidate', 'Candidate'),
        ('recruiter', 'Recruiter'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Candidate-specific fields
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)

    # Recruiter-specific fields
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)

    # Auth setup
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# # Import necessary Django modules for custom user model
# # We import models to define database fields and relationships
# from django.db import models
# # We import these classes to create a custom user model with authentication capabilities
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# # Custom manager class to handle user creation
# # We extend BaseUserManager to provide custom user creation methods
# class CustomUserManager(BaseUserManager):
#     # Method to create regular users
#     # We customize this to require email instead of username
#     def create_user(self, email, name, password=None, **extra_fields):
#         # Validate email is provided
#         # Email is required as it's our main identifier
#         if not email:
#             raise ValueError("Users must have an email address")
#         # Normalize the email address
#         # This standardizes email format for consistency
#         email = self.normalize_email(email)
#         # Create new user instance
#         # We pass email and name as required fields
#         user = self.model(email=email, name=name, **extra_fields)
#         # Set encrypted password
#         # This handles password hashing securely
#         user.set_password(password)
#         # Save user to database
#         # using=self._db ensures correct database is used
#         user.save(using=self._db)
#         return user

#     # Method to create superuser/admin
#     # We need this for creating admin users via command line
#     def create_superuser(self, email, name, password=None, **extra_fields):
#         # Set admin privileges
#         # Superusers need these permissions for admin access
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         # Create superuser using create_user method
#         # Reuse create_user to ensure consistent user creation
#         return self.create_user(email, name, password, **extra_fields)


# # Custom User model extending Django's abstract base classes
# # We inherit from AbstractBaseUser for basic user fields and PermissionsMixin for permissions
# class User(AbstractBaseUser, PermissionsMixin):
#     # Define user model fields
#     # name: Store user's full name
#     name = models.CharField(max_length=255)
#     # email: Primary identifier for user, must be unique
#     email = models.EmailField(unique=True)
#     # phone: Optional contact number
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     # is_active: Control whether user account is active
#     is_active = models.BooleanField(default=True)
#     # is_staff: Control admin site access
#     is_staff = models.BooleanField(default=False)

#     # Specify email as the username field
#     # We use email instead of username for login
#     USERNAME_FIELD = 'email'
#     # Additional required fields for user creation
#     # Name is required alongside email
#     REQUIRED_FIELDS = ['name']

#     # Assign custom manager to objects
#     # This connects our CustomUserManager to the User model
#     objects = CustomUserManager()

#     # String representation of user object
#     # This defines how the user object appears in string format
#     def __str__(self):
#         return self.email