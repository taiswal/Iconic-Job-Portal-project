from django import forms
from .models import Recruiter
from company.models import Company

class RecruiterForm(forms.ModelForm):
    companies = forms.ModelMultipleChoiceField(
        queryset=Company.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Companies"
    )

    class Meta:
        model = Recruiter
        fields = [
            'user',
            'companies',
            'company_website',
            'contact_number',
            'company_description',
            'company_location',
            'profile_picture',
            'established_year',
            'industry',
            'bio'
        ]
        widgets = {
            'company_description': forms.Textarea(attrs={'rows': 3}),
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
