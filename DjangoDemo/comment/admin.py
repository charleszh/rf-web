from django.contrib import admin

from blogproject.custom_site import custom_site
from blogproject.base_admin import BaseOwnerAdmin
from .models import Comment
# Register your models here.

@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_time', 'website', 'target']#tmp comment, 'author']
    fields = ['target','email', 'website', 'content', 'nickname', 'status']


admin.site.register(Comment, CommentAdmin)

