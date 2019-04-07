"""esportsCommunity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from home.views import index
from accounts.views import (logout, login, register, user_profile,
                        update_user_profile, post_detail, create_or_edit_post,
                        delete_post)
from django.conf import settings
from django.conf.urls.static import static
from accounts import url_reset as reset_urls
from issue_tracker import url_issues as issue_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^password-reset/', include(reset_urls)),
    url(r'issue-tracker/', include(issue_urls)),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/register/$', register, name='register'),
    url(r'^accounts/profile/$', user_profile, name='profile'),
    url(r'^accounts/profile/update/$', update_user_profile, name="update profile"),
    url(r'^new_post/$', create_or_edit_post, name="new_post"),
    url(r'^profile/post/(?P<pk>\d+)/$', post_detail, name="post_detail"),
    url(r'^profile/post/(?P<pk>\d+)/edit/$', create_or_edit_post, name="edit_post"),
    url(r'^profile/post/(?P<pk>\d+)/delete/$', delete_post, name="delete_post"),
    

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
