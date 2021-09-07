"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework import permissions, routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import pdb

#from .custom_site import custom_site

schema_view = get_schema_view(
    openapi.Info(
        title = "Hello Django Rest Framework tutorial API",
        default_version="v1",
        description="Hello django rest framework tutorial api",
        terms_of_service="",
        contact=openapi.Contact(email="zmrenwu#163.com"),
        license=openapi.License(name="GPLv3 License"),
    ),
    public = True,
    permission_classes=(permissions.AllowAny,),
)
print("in project urls")
urlpatterns = [
    #path('super_admin/', admin.site.urls),
    #path('admin/', custom_site.urls),
    path('admin/', xadmin.site.urls, name='xadmin'),
    path(r'api/accounts/', include('users.urls')),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api/api-token-refresh/', refresh_jwt_token),
    path(r'api-token-verify/', verify_jwt_token),
    path(r'api/student/', include('student.urls', namespace='student-ns')),
    path(r'newblog/', include('newblog.urls')),
    path(r'', include('blog.urls')),


    re_path(
        r"swagger(?P<format>\.json|.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
