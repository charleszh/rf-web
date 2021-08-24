from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from newblog.views import post_list, post_detail
from config.views import links
from blogproject.custom_site import custom_site


app_name = 'newblog'

urlpatterns = [
    url(r'^$', post_list),
    url(r'^category/(?P<category_id>\d+)/$', post_list, name='catgory_list'),
    url(r'^tag/(?P<tag_id>\d+)/$', post_list),
    url(r'^post/(?P<post_id>\d+).html$', post_detail),
    url(r'^links/$', links),
]
