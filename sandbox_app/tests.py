from django.test import TestCase
from django.utils import timezone

from .models import (
    Post, upload_directory_path
)


class SandboxAppTest(TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title="post title", body="post body content", created=timezone.now())

    def tearDown(self):
        pass

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.title, post.__str__())
        self.assertEqual(post.title, "post title")

    def test_post_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.get_absolute_url(), '/posts/1/')

    def test_attachment_creation(self):
        path = upload_directory_path(None, "test.png")
        self.assertNotEqual("test.png", path)
        self.assertTrue(path.startswith('attachments'))
        self.assertTrue(path.endswith('png'))
