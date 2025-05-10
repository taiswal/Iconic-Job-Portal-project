from django.contrib import admin
from .models import Job, Contact

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'company', 'recruiter', 'job_type', 'experience_level',
        'city', 'country', 'is_available', 'deadline', 'created_at'
    )
    list_filter = ('job_type', 'experience_level', 'industry', 'is_available', 'created_at')
    search_fields = ('title', 'company__name', 'recruiter__username', 'city', 'country')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'description', 'requirements', 'ideal_candidate', 'tags')
        }),
        ('Company & Recruiter', {
            'fields': ('company', 'recruiter')
        }),
        ('Job Details', {
            'fields': ('job_type', 'industry', 'experience_level', 'salary', 'deadline', 'is_available')
        }),
        ('Location', {
            'fields': ('city', 'state', 'country')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)
