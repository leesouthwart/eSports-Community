from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile, Post, PostComment



class UserLoginForm(forms.Form):
    """form to be used to log in"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class UserRegistrationForm(UserCreationForm):
    """Form to register a new user"""
    
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", 
                                widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        required = ['email', 'username', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        if password1 != password2:
            raise ValidationError("Passwords must match")
            
        return password2
    
# user update form for email update
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
#Profile update
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'user_bio', 'location', 'available_to_team']


#Post form
class PostForm(forms.ModelForm):
    
     class Meta:
        model = Post
        fields = ['title', 'post_content', 'image']
        
class PostCommentForm(forms.ModelForm):
    
    class Meta:
        model = PostComment
        fields = ['comment_content']