import xadmin

from django.contrib import admin

from blogproject.custom_site import custom_site
from blogproject.base_admin import BaseOwnerAdmin
from .models import Link, SideBar
# Register your models here.


#@admin.register(Link, site=custom_site)
@xadmin.sites.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ['title', 'href', 'status', 'weight', 'created_time']
    fields = ['title', 'href', 'status', 'weight']


#@admin.register(SideBar, site=custom_site)
@xadmin.sites.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ['title', 'display_type', 'content', 'created_time']
    fields = ['title', 'display_type', 'content']


#admin.site.register(Link, LinkAdmin)
#admin.site.register(SideBar, SideBarAdmin)
