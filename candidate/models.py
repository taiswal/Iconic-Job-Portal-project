from django.db import models
from users.models import User

# Create your models here.


# ----------------------------
# Candidate Profile
# ----------------------------

class Candidate(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'), 
        ('Female', 'Female'),
        ('Other', 'Other')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    skills = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    experience = models.PositiveIntegerField(default=0)
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='Candidate_pics/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.username})" if self.user else self.full_name