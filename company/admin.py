from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'industry', 'owner', 'is_verified', 'created_at')
    list_filter = ('is_verified', 'industry', 'created_at')
    search_fields = ('name', 'email', 'industry', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'email', 'website', 'address', 'industry')
        }),
        ('Details', {
            'fields': ('description', 'logo', 'founded_year', 'team_size', 'mission', 'linkedin')
        }),
        ('Verification & Ownership', {
            'fields': ('is_verified', 'owner')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
