# -*- coding: utf8 -*-
from django.test import TestCase
from django.apps import apps
from blog.models import ExecuteStatus, Tag
from blog.models import TestCase as TC
from django.contrib.auth.models import User
import datetime
import os


class TestCaseModelTestCase(TestCase):
    def setUp(self):
        #apps.get_app_config()
        #user = User.objects.create_superuser()
        from django.utils import timezone
        created_time = timezone.now()
        tags = Tag.objects.order_by('?')
        tag1 = tags.first()
        tag2 = tags.last()
        status = ExecuteStatus.objects.create(name='Testing')
        #user = User.objects.get_by_natural_key('admin')
        user = User.objects.create_superuser(
            username='admin1',
            email='admin@hellogithub.com',
            password='admin')
        self.testcase = TC.objects.create(
            name='1234',
            created_time=created_time,
            abstract='This is the',
            execute_status=status,
            author=user,
        )
        #testcase.tags.add(tag1, tag2)
        #testcase.save()

    def test_str_representation(self):
        self.assertEqual(self.testcase.__str__(), self.testcase.name)