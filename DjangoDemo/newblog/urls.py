from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from newblog.views import AuthorView, SearchView, IndexView, CategoryView, TagView, PostListView, PostDetailView, post_list, post_detail
from config.views import LinkListView
from config.views import links
from comment.views import CommentView
#from blogproject.custom_site import custom_site


app_name = 'newblog'

urlpatterns = [
    #url(r'^$', post_list),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    #url(r'^post/(?P<post_id>\d+).html$', post_detail, name='post-detail'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<author_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),

]
