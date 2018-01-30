from django.apps import apps
from django.contrib import auth
from django.contrib.auth.models import User
from django.test import (
    TestCase, Client
)
from django.utils import timezone

from .apps import SandboxAppConfig
from .models import (
    Post, upload_directory_path
)


class SandboxAppTest(TestCase):
    def setUp(self):
        self.username = 'dsa'
        self.password = 'pass'

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title="post title", body="post body content", created=timezone.now())

    def tearDown(self):
        pass

    # apps
    def test_apps(self):
        self.assertEqual(SandboxAppConfig.name, 'sandbox_app')
        self.assertEqual(SandboxAppConfig.verbose_name, 'sandbox')
        self.assertEqual(apps.get_app_config('sandbox_app').name, 'sandbox_app')

    # models
    def test_post_creation(self):
        post = Post.objects.get(id=1)
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.title, post.__str__())
        self.assertEqual(post.title, "post title")

    def test_post_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.get_absolute_url(), '/posts/1/')

    def test_upload_directory_path(self):
        path = upload_directory_path(None, "test.png")
        self.assertNotEqual("test.png", path)
        self.assertTrue(path.startswith('attachments'))
        self.assertTrue(path.endswith('png'))

    # widgets

    # forms

    # views
    def test_user_is_not_authenticated(self):
        user = auth.get_user(self.client)
        self.assertTrue(not user.is_authenticated)

    def test_login(self):
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.assertTrue(Client().login(username=self.username, password=self.password))
