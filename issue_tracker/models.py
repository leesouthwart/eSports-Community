from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

#Class for users posts
class Bug(models.Model):
    title = models.CharField(max_length=100)
    bug_content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User.username)
    views = models.IntegerField(default=1)
    upvotes = models.IntegerField(default=1)
    status = models.CharField(default='Backlog', max_length=20)