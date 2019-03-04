from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from home.views import index
from accounts.forms import (UserLoginForm, UserRegistrationForm, 
                            UserUpdateForm, ProfileUpdateForm, PostForm)
from accounts.models import Profile, Post

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

@login_required
def user_profile(request):
    """
    The Users profile page
    """
    user = User.objects.get(email=request.user.email)
    posts = Post.objects.filter(author=user).order_by('-date_posted')
    
    
    return render(request, 'profile.html', {'user': user, 'posts': posts})

@login_required
def update_user_profile(request):
    
    user = User.objects.get(email=request.user.email)
    #forms to update user profile
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user
    }
        
    return render(request, 'update_profile.html', context)

# Individual posts view based on the post id
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, 'postdetail.html', {'post': post})
    


# View for creating or editing a view. Depends on if the PK is None or not.  
def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create or edit a post depending if
    the Post Id is null or not
    """
    
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_posted = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'new_blogpost.html', {'PostForm': form, 'post': post})  

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Post.objects.filter(id=pk).delete()
    return redirect('profile')

