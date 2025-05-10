from django.db import models
from users.models import User
from company.models import Company
from posts.models import Tag


class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ('Remote', 'Remote'),
        ('Onsite', 'Onsite'),
        ('Hybrid', 'Hybrid'),
    )

    INDUSTRY_CHOICES = (
        ('Technology', 'Technology'),
        ('Education', 'Education'),
        ('Finance', 'Finance'),
        ('Healthcare', 'Healthcare'),
        ('Transportation', 'Transportation'),
        ('Energy', 'Energy'),
        ('Other', 'Other'),
    )

    TITLE_CHOICES = (
        ('Developer', 'Developer'),
        ('Consultant', 'Consultant'),
        ('Analyst', 'Analyst'),
        ('Manager', 'Manager'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('HR', 'HR'),
        ('Operations', 'Operations'),
    )

    EXPERIENCE_CHOICES = (
        ('Fresher', 'Fresher'),
        ('1-3 years', '1-3 years'),
        ('3-5 years', '3-5 years'),
        ('5+ years', '5+ years'),
    )

    title = models.CharField(max_length=100, choices=TITLE_CHOICES, null=True, blank=True)
    description = models.TextField()
    requirements = models.TextField()
    ideal_candidate = models.TextField(blank=True, null=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    recruiter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='posted_jobs')

    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, blank=True, null=True)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES, blank=True, null=True)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, blank=True, null=True)

    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, default='India')
    salary = models.PositiveIntegerField(default=30000)

    is_available = models.BooleanField(default=True)
    deadline = models.DateField(blank=True, null=True)

    tags = models.ManyToManyField(Tag, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title or 'Job'} at {self.company.name}"



from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100,null=True,blank=False)
    email = models.EmailField(unique=True,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
