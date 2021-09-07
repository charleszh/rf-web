import xadmin
from xadmin.layout import Row, Fieldset, Container
from xadmin.filters import manager, RelatedFieldListFilter

from django.contrib import admin
from django.contrib.admin.models import LogEntry

from django.urls import reverse
from django.utils.html import format_html
from .models import Category, Tag, Post
from .adminforms import PostAdminForm
#from blogproject.custom_site import custom_site
from blogproject.base_admin import BaseOwnerAdmin
from blogproject.loghandler import logger
# Register your models here.



#class CategoryOwnerFilter(admin.SimpleListFilter):
class CategoryOwnerFilter(RelatedFieldListFilter):
    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.lookup_choices = Category.objects.filter(author=request.user).values_list('id', 'name')

manager.register(CategoryOwnerFilter, take_priority=True)

    #""" 自定义过滤器只展示当前用户分类 """
    #title = '分类过滤器'
    #parameter_name = 'owner_category'

    #def lookups(self, request, model_admin):
    #    return Category.objects.filter(author=request.user).values_list('id', 'name')

    #def queryset(self, request, queryset):
    #    category_id = self.value()
    #    if category_id:
    #        return queryset.filter(category_id=self.value())
    #    return queryset


#@admin.register(Post, site=custom_site)
@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    list_display = ['title', 'content', 'created_time', 'category', 'status', 'operator', 'author', 'pv', 'uv']#tmp comment, 'author']
    list_display_links = ['title']

    #list_filter = [ CategoryOwnerFilter ]
    list_filter = [ 'category' ]
    search_fields = ['title', 'category_name']

    filter_horizontal = ('tag', )

    form = PostAdminForm
    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True
    exclude = ['author']
    # fields = (
    #     ('title', 'category' ),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

    #fieldsets = (
    #    ('基础配置', {
    #        'description': '基础配置描述',
    #        'fields': (
    #            ('title', 'category'),
    #            'status',
    #        ),
    #    }),
    #    ('内容', {
    #        'fields': (
    #            'desc',
    #            'content',
    #        ),
    #    }),
    #    ('额外信息', {
    #        'classes': ( 'wide',),
    #        'fields': ('tag',),
    #    })
    #)

    form_layout = (
        Fieldset(
            '基础配置', 
            Row('title', 'category'),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息', 
            'desc',
            'content',
        )
    )

    def comments(self, obj):
        return format_html(
            '<a href="{}">查看评论</a>',
            reverse('admin.comment_comment_list',  args=(obj.id,))
        )
    comments.short_description = '评论'

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:newblog_post_change', args=(obj.id,))
            #reverse('cus_admin:newblog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    #class Media:
    #    css = {
    #        'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
    #    }
    #    js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )
    #@property
    #def media(self):
    #    media = super().media
    #    media.add_css({
    #        'all': ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css',),
    #        })
    #    media.add_js(['https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js'])
    #    return media


#class PostInline(admin.TabularInline):
#    fields = ('title', 'status')
#    extra = 1
#    model = Post

class PostInline:
    form_layout = (
            Container(
                Row("title", "desc"),
            )
    )
    extra = 1
    model = Post


#@admin.register(Category, site=custom_site)
@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'is_nav', 'author', 'created_time', 'post_count']
    fields = ['name', 'status', 'is_nav']
    inlines = [PostInline]

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

#@admin.register(Tag, site=custom_site)
@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    pass


#@admin.register(LogEntry, site=custom_site)
#@xadmin.sites.register(LogEntry)
#class LogEntryAdmin(object):
#    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']

#admin.site.register(Post, PostAdmin)
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Tag, TagAdmin)

