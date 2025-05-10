from django.db import models
from django.conf import settings

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    founded_year = models.IntegerField(blank=True, null=True)
    team_size = models.CharField(max_length=50, blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='companies',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Company"
