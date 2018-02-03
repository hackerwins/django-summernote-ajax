from django.apps import apps
from django.test import TestCase

from .apps import DjangoSummernoteAjaxConfig
from .widgets import SummernoteWidgetBase


class DjangoSummernoteAjaxTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # apps
    def test_apps(self):
        self.assertEqual(DjangoSummernoteAjaxConfig.name, 'django_summernote_ajax')
        self.assertEqual(DjangoSummernoteAjaxConfig.verbose_name, 'Django Summernote Ajax')
        self.assertEqual(apps.get_app_config('django_summernote_ajax').name, 'django_summernote_ajax')

    # models

    # widgets
    def test_summernote_widget(self):
        widget = SummernoteWidgetBase(wrapper_class='summernote-box', options={'upload_url': '/upload-file'})
        html = widget.render(name='foo', value='bar')
        self.assertIn('summernote-widget', html)
        self.assertIn('summernote-box', html)
        self.assertIn('"upload_url": "/upload-file"', html)

    # forms

    # viewmixins

    # views
