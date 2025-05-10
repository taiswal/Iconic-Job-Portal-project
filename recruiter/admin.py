from django.contrib import admin
from .models import Recruiter

@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_website', 'contact_number', 'industry']
    list_filter = ['industry', 'established_year']
    search_fields = ['user__email', 'company_location', 'industry']
