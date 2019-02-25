from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.views import index
from accounts.forms import UserLoginForm, UserRegistrationForm
from accounts.models import Profile
## ACCOUNT.VIEWS

@login_required
def logout(request):
    """
    log users out
    """
    auth.logout(request)
    return redirect(reverse('index'))

def login(request):
    """
    login a user
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
                                     
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "welcome back," + user.username)
                return redirect(reverse('index'))
                
            else: login_form.add_error(None, "Your username or password is incorrect.")    
                                      
    else:
        login_form = UserLoginForm()
        
    return render(request, 'login.html', {"login_form": login_form})
    
def register(request):
    """
    Render the registration page
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
     
        if registration_form.is_valid():
            registration_form.save()
        
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else: messages.error(request, "Unable to register your account")
    else:        
        registration_form = UserRegistrationForm()
     
        
    return render(request, 'register.html', {"registration_form": registration_form})

def user_profile(request):
    """
    The Users profile page
    """
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'user': user})
    