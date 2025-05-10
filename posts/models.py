from django.db import models
from users.models import User  
from recruiter.models import Recruiter
from company.models import Company


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='images/profiles/', null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    graduation_year = models.CharField(max_length=10, blank=True, null=True)
    is_recruiter = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name


class Tag(models.Model):
    SKILL_CHOICES = [
        ('Python', 'Python'), ('JavaScript', 'JavaScript'), ('Django', 'Django'),
        ('React', 'React'), ('SQL', 'SQL'), ('Java', 'Java'), ('C#', 'C#'),
        ('AWS', 'AWS'), ('Docker', 'Docker'), ('Machine Learning', 'Machine Learning'),
        ('Data Analysis', 'Data Analysis'), ('UI/UX Design', 'UI/UX Design'),
        ('SEO', 'SEO'), ('Graphic Design', 'Graphic Design')
    ]

    TAG_TYPE_CHOICES = [
        ('Skill', 'Skill'),
        ('Tool', 'Tool'),
        ('Language', 'Language'),
        ('Other', 'Other'),
    ]

    tag_name = models.CharField(max_length=255, unique=True, choices=SKILL_CHOICES)
    tag_type = models.CharField(max_length=50, blank=True, choices=TAG_TYPE_CHOICES)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Apprenticeship', 'Apprenticeship'),
        ('Internship', 'Internship'), ('Traineeship', 'Traineeship'), ('Contract', 'Contract'),
        ('Casual', 'Casual'), ('Seasonal', 'Seasonal'), ('Commission', 'Commission'),
        ('Leased', 'Leased'), ('Contingent', 'Contingent'), ('Probation', 'Probation'),
        ('Freelance', 'Freelance'), ('Temporary', 'Temporary'),
    ]

    INDUSTRY_CHOICES = [
        ('IT', 'Information Technology'), ('Healthcare', 'Healthcare'), ('Finance', 'Finance'),
        ('Education', 'Education'), ('Marketing', 'Marketing'), ('Engineering', 'Engineering'),
        ('Retail', 'Retail'), ('Customer Service', 'Customer Service'), ('Legal', 'Legal'),
    ]

    EXPERIENCE_CHOICES = [
        ('Fresher', 'Fresher'), ('Entry', 'Entry-level'), ('Mid', 'Mid-level'),
        ('Senior', 'Senior-level'), ('Manager', 'Manager'), ('Director', 'Director'),
    ]

    WORK_ENV_CHOICES = [('Remote', 'Remote'), ('On-site', 'On-site'), ('Hybrid', 'Hybrid')]

    SALARY_CHOICES = [
        ('Below 30K', 'Below 30K'), ('30K-50K', '30K-50K'), ('50K-80K', '50K-80K'),
        ('80K-100K', '80K-100K'), ('100K+', '100K+'),
    ]

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('B', 'Both')]

    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_date = models.DateField()
    location = models.CharField(max_length=200, default='Not Specified')
    job_type = models.CharField(max_length=100, choices=JOB_TYPE_CHOICES, default='Full Time')
    industry = models.CharField(max_length=100, blank=True, null=True)
    experience_level = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES, default='Fresher')
    work_environment = models.CharField(max_length=20, choices=WORK_ENV_CHOICES, blank=True, null=True)
    salary = models.CharField(max_length=50, choices=SALARY_CHOICES, null=True, blank=True)
    skill_tags = models.ManyToManyField(Tag, blank=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    vacancy = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='B')
    graduation_year = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='images/job_posts/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"


    class Meta:
        verbose_name = "Job Post"
        verbose_name_plural = "Job Posts"


# from django.db import models
# from users.models import User

# # Create your models here.

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField()
#     profile_picture = models.ImageField(upload_to='image/',null=True, blank=True)

#     def __str__(self):
#         return str(self.user)

# class Tag(models.Model):
#     tag_name = models.CharField(max_length=255, unique=True)

#     def __str__(self):
#         return self.tag_name

# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     tags = models.ManyToManyField(Tag)
#     image = models.ImageField(upload_to='image/',null=True, blank=True)
#     def __str__(self):
#         return self.title
    

    