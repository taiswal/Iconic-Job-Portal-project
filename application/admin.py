from django.contrib import admin
from .models import Application, Bookmark

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'status', 'applied_at', 'is_viewed')
    list_filter = ('status', 'is_viewed', 'applied_at')
    search_fields = ('job__title', 'applicant__email', 'cover_letter')
    readonly_fields = ('applied_at', 'updated_at')
    fieldsets = (
        ('Application Info', {
            'fields': ('job', 'applicant', 'resume', 'cover_letter')
        }),
        ('Status & Review', {
            'fields': ('status', 'is_viewed', 'screening_score', 'notes', 'interview_date')
        }),
        ('Timestamps', {
            'fields': ('applied_at', 'updated_at')
        }),
    )

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'bookmarked_at')
    list_filter = ('bookmarked_at',)
    search_fields = ('user__email', 'job__title')
