from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1. 自动补充newblog各model的author字段
    2. 对queryset过滤当前用户数据
    """
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(author=request.user)
