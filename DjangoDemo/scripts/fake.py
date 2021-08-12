'''
generate testing data
use the package Faker: pipenv install Faker
'''
import django
import faker
from django.utils import timezone
import os
import sys
back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","blogproject.settings" )
    django.setup()
    from blog.models import TestCase, ExecuteStatus, Tag
    from django.contrib.auth.models import User
    fake = faker.Faker('zh_CN')
    created_time = fake.date_time_between(start_date='-1y', end_date="now", tzinfo=timezone.get_current_timezone())
    tags = Tag.objects.order_by('?')
    tag1 = tags.first()
    tag2 = tags.last()
    status = ExecuteStatus.objects.order_by('?').first()
    user = User.objects.get_by_natural_key('admin')
    testcase = TestCase.objects.create(
        name=fake.sentence().rstrip('.'),
        created_time = created_time,
        abstract='\n\n'.join(fake.paragraphs(1)),
        execute_status=status,
        author=user,
    )
    testcase.tags.add(tag1, tag2)
    testcase.save()
