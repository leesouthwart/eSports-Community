from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Bug, BugComment, Content, ContentComment

#Bug Form
class BugForm(forms.ModelForm):
    
    class Meta:
        model = Bug
        fields = ['title', 'bug_content', 'status']


class ContentSuggestionForm(forms.ModelForm):
    
    class Meta:
        model = Content
        fields = ['title', 'suggestion_content', 'status']
        
class BugCommentForm(forms.ModelForm):
    
    class Meta:
        model = BugComment
        fields = ('comment_content',)
        
class ContentCommentForm(forms.ModelForm):
    
    class Meta:
        model = ContentComment
        fields = ('comment_content',)