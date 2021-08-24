from django.shortcuts import render
from django.http import HttpResponse

from . import logger
from .models import Post, Category, Tag
from config.models import SideBar
# Create your views here.

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
    return render(request, 'newblog/detail.html', context={'post': post})
