from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Bug

#Bug Form
class BugForm(forms.ModelForm):
    
    class Meta:
        model = Bug
        fields = ['title', 'bug_content', 'status']


