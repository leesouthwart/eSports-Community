from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from .views import (issue_tracker_bugs, single_bug, delete_bug, create_or_edit_bug,
                    upvote_bug, downvote_bug, issue_tracker_content, single_content, upvote_content, delete_content, create_or_edit_content)
#issue_tracker_content

urlpatterns = [
    url(r'^bugs/$',issue_tracker_bugs, name="issue_tracker_bugs"),
    url(r'^$',issue_tracker_content, name="issue_tracker_content"),
    url(r'^bugs/(?P<pk>\d+)/$', single_bug, name="single_bug"),
    url(r'^(?P<pk>\d+)/$', single_content, name="single_content"),
    url(r'^bugs/(?P<pk>\d+)/delete/$', delete_bug, name="delete_bug"),
    url(r'^bugs/(?P<pk>\d+)/edit/$', create_or_edit_bug, name="edit_bug"),
    url(r'^bugs/new/$', create_or_edit_bug, name="new_bug"),
    url(r'^bugs/(?P<pk>\d+)/upvote/', upvote_bug, name="upvote_bug"),
    url(r'^bugs/(?P<pk>\d+)/downvote/', downvote_bug, name="downvote_bug"),
    url(r'^(?P<pk>\d+)/upvote/', upvote_content, name="upvote_content"),
    url(r'^(?P<pk>\d+)/delete/$', delete_content, name="delete_content"),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_content, name="edit_content"),
    url(r'^new/$', create_or_edit_content, name="new_content"),
    ]
