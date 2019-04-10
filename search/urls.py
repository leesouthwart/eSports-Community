from django.conf.urls import url
from .views import search_bugs, search_content, filter_content, filter_bugs
urlpatterns = [
    
    url(r'bugs/$', search_bugs, name="search_bugs"),
    url(r'content/$', search_content, name="search_content"),
    url(r'content/filter$', filter_content, name="filter_content"),
    url(r'bugs/filter$', filter_bugs, name="filter_bugs"),
    
    ]
