from django.contrib import admin
from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'location', 'experience', 'expected_salary', 'created_at')
    list_filter = ('gender', 'location', 'experience', 'created_at')
    search_fields = ('full_name', 'user__username', 'skills', 'location')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Basic Info', {
            'fields': ('user', 'full_name', 'date_of_birth', 'gender', 'phone')
        }),
        ('Professional Details', {
            'fields': ('education', 'skills', 'experience', 'expected_salary', 'location')
        }),
        ('Media & Links', {
            'fields': ('resume', 'profile_picture', 'linkedin_url', 'portfolio_url')
        }),
        ('Additional Info', {
            'fields': ('address', 'created_at')
        }),
    )
