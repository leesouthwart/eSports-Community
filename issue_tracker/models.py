from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

#Class for users posts
class Bug(models.Model):
    
    #options for statuses that can be changed by admin
    statuses = (
        ('a', 'Backlog'), 
        ('b', 'In Progress'),
        ('c', 'Completed')
        
        )
    
    title = models.CharField(max_length=100)
    bug_content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=1)
    upvotes = models.IntegerField(default=1)
    status = models.CharField(default='a', choices=statuses, max_length=20, blank=True)
    
    def __str__(self):
        return self.title
    
class Content(models.Model):
    
    #options for statuses that can be changed by admin
    statuses = (
        ('a', 'Backlog'), 
        ('b', 'In Progress'),
        ('c', 'Completed')
        
        )
    
    title = models.CharField(max_length=100)
    suggestion_content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=1)
    upvotes = models.IntegerField(default=1)
    status = models.CharField(default='a', choices=statuses, max_length=20, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=1.00) 
    #this is needed to allow us to charge for an upvote.
    
    def __str__(self):
        return self.title