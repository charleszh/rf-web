'''
generate testing data
use the package Faker: pipenv install Faker
'''
import django
import faker
from django.utils import timezone
import os
import random
import sys


back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","blogproject.settings.develop" )
    django.setup()
    fake = faker.Faker('zh_CN')
    for s in range(0, 1):
        from newblog.models import Category, Tag
        from newblog.models import Post
        from django.contrib.auth.models import User
        created_time = fake.date_time_between(start_date='-1y', end_date="now", tzinfo=timezone.get_current_timezone())
        user = User.objects.order_by('?').first()
        tags = Tag.objects.order_by('?')
        category = Category.objects.order_by('?').first()
        category1 = Category.objects.order_by('?').last()
        post = Post.objects.create(
            title=fake.sentence(),
            desc = fake.paragraph(),
            content = fake.text(),
            created_time = created_time,
            status = random.choice([0, 1, 2]),
            category = random.choice([category, category1]),
            author = user,
        )
        post.tag.set(tags)
        post.save()
