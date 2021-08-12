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
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","blogproject.settings" )
    django.setup()
    from student.models import Student
    from django.contrib.auth.models import User
    fake = faker.Faker('zh_CN')
    for s in range(0, 50):
        created_time = fake.date_time_between(start_date='-1y', end_date="now", tzinfo=timezone.get_current_timezone())
        student = Student.objects.create(
            name=fake.name(),
            created_time = created_time,
            sex = random.choice([1, 2, 0]),
            email = fake.email(),
            profession = fake.company(),
            qq = fake.postcode(), # use postcode as qq examples
            phone= fake.phone_number(),
            homephone = fake.phone_number(),
            status = random.choice([1, 2, 0]),
        )
        student.save()
