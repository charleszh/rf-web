from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic import ListView

from . import logger
from .models import Post, Category, Tag
from config.models import SideBar
# Create your views here.


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all(),
        })
        context.update(Category.get_navs())
        logger.info("out of f common")
        logger.info(context)
        return context


class IndexView(CommonViewMixin, ListView):
    logger.info("enter into f indexview")
    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'newblog/list.html'
    logger.info("out of indexview")


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag_id=tag_id)


class PostListView(ListView):
    queryset = Post.latest_posts()
    paginate_by = 10
    context_object_name = 'post_list'
    template_name = 'newblog/list.html'
    logger.info("out of post list view")


class PostDetailView(CommonViewMixin, DetailView):
    logger.info('enter into post detail view')
    queryset = Post.latest_posts()
    template_name = 'newblog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


def post_list(request, category_id=None, tag_id=None):
    logger.info("Enter into function post_list")
    tag = None
    category = None
    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        logger.info('category class')
        post_list, category = Post.get_by_category(category_id)
        logger.info(post_list)
    else:
        post_list = Post.latest_posts()


    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, 'newblog/list.html', context=context)#{'post_list': post_list})

def post_detail(request, post_id):
    try:
        logger.info('in post detail')
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post,
        'sidebars': SideBar.get_all()
    }
    context.update(Category.get_navs())
    logger.info(context)
    return render(request, 'newblog/detail.html', context=context)
