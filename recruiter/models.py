from django.db import models
from users.models import User
from company.models import Company

# Create your models here.
class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    companies = models.ManyToManyField(Company, related_name='recruiters')
    company_website = models.URLField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    company_location = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="recruiter_profiles/", blank=True, null=True)
    established_year = models.PositiveIntegerField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.email if self.user else 'NoUser'}"

    class Meta:
        verbose_name = 'Recruiter'
        verbose_name_plural = 'Recruiters'


        
    
    
    
    
    
