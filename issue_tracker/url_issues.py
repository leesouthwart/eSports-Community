from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from .views import issue_tracker_bugs, single_bug, delete_bug, create_or_edit_bug
#issue_tracker_content

urlpatterns = [
    url(r'^bugs/$',issue_tracker_bugs, name="issue_tracker_bugs"),
    #url(r'^$',issue_tracker_content, name="issue_tracker_content"),
    url(r'^bugs/(?P<pk>\d+)/$', single_bug, name="single_bug"),
    url(r'^bugs/(?P<pk>\d+)/delete/$', delete_bug, name="delete_bug"),
    url(r'^bugs/(?P<pk>\d+)/edit/$', create_or_edit_bug, name="edit_bug"),
    url(r'^bugs/new/$', create_or_edit_bug, name="new_bug"),
    
    
    ]
