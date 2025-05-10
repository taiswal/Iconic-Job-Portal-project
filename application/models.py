from django.db import models
from django.conf import settings
from job.models import Job

# Create your models here.
class Application(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    is_viewed = models.BooleanField(default=False)
    screening_score = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    interview_date = models.DateTimeField(null=True, blank=True)

    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.applicant.email} -> {self.job.title}'


class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='bookmarked_by')
    bookmarked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')

    def __str__(self):
        return f'{self.user.email} bookmarked {self.job.title}'

