from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ExecuteStatus(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class TestCase(models.Model):
    name = models.CharField(max_length=50, verbose_name="测试用例名称")
    abstract = models.CharField(max_length=200)
    # steps = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='NA')
    execute_status = models.ForeignKey(ExecuteStatus, on_delete=models.SET_DEFAULT, default=2)
    from django.utils import timezone
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('最后修改时间', auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.name

    def was_publuished_recently(self):
        import datetime
        from django.utils import timezone
        return self.created_time <= timezone.now() - datetime.timedelta(days=1)

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from datetime import datetime

def change_post_updated_at(sender=None, instance=None, *args, **kwargs):
    cache.set("testcase_updated_at", datetime.utcnow())

post_save.connect(receiver=change_post_updated_at, sender= TestCase)
post_delete.connect(receiver=change_post_updated_at, sender= TestCase)
