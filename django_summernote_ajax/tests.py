from django.apps import apps
from django.test import TestCase

from .apps import DjangoSummernoteAjaxConfig


class DjangoSummernoteAjaxTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_apps(self):
        self.assertEqual(DjangoSummernoteAjaxConfig.name, 'django_summernote_ajax')
        self.assertEqual(DjangoSummernoteAjaxConfig.verbose_name, 'Django Summernote Ajax')
        self.assertEqual(apps.get_app_config('django_summernote_ajax').name, 'django_summernote_ajax')
