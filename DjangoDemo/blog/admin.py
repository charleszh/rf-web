from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag, TestCase

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

class TestCaseAdmin(admin.ModelAdmin):
    readonly_fields = ['modified_time']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(TestCase, TestCaseAdmin)