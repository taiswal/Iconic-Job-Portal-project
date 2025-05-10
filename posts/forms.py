from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'recruiter', 'company', 'title', 'description', 'last_date',
            'location', 'job_type', 'industry', 'experience_level',
            'work_environment', 'salary', 'skill_tags', 'url', 'is_closed',
            'vacancy', 'gender', 'graduation_year', 'image'
        ]
        widgets = {
            'last_date': forms.DateInput(attrs={'type': 'date'}),
            'skill_tags': forms.CheckboxSelectMultiple()
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_name', 'tag_type']
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # fields = ['bio', 'profile_picture', 'user']
        fields = [
            'user', 'bio', 'profile_picture', 'resume', 'location',
            'linkedin', 'portfolio', 'phone', 'github', 'graduation_year', 'is_recruiter'
        ]
