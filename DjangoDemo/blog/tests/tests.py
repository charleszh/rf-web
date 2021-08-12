from django.test import TestCase
from django.apps import apps
from ..models import TestCase as TC

# Create your tests here.

class BlogModelTests(TestCase):
    def test_temp(self):
        self.assertIs(1, 1)

    def test_was_published_recently_with_future_testcase(self):
        from django.utils import timezone
        import datetime
        time = timezone.now() + datetime.timedelta(days=30)
        future_testcase = TC(created_time=time)
        self.assertIs(future_testcase.was_publuished_recently(), False)