from django.contrib import admin
from .models import Bug, BugComment, Content, ContentComment
# Register your models here.

admin.site.register(Bug)
admin.site.register(Content)
admin.site.register(BugComment)
admin.site.register(ContentComment)