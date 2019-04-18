from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image 
# Create your models here.


# class for user profiles. 'extends' the default User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    available_to_team = models.BooleanField(default=True)
    image = models.ImageField(default='standard.jpg', upload_to='profile_pics', blank=True)
    
   
    
#when User is created, make profile for said user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#when User is saved, save profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

#Class for users posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    post_content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', blank=True)
    views = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title
        

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.comment_content
   
