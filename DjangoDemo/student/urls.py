from django.urls import path
from django.contrib import  admin

from student.views import IndexView

app_name = 'student'
print('in student urls.py')
urlpatterns = [
    path(r'index/', IndexView.as_view(), name='index'),
]
