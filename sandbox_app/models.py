import os
import uuid

from django.conf import settings
from django.core.files.storage import default_storage
from django.db import models
from django.urls import reverse
from django.utils.timezone import datetime
from django.utils.translation import ugettext_lazy as _

from django_summernote_ajax.models import AbstractAttachment


def upload_directory_path(instance, filename):
    """
    Determine directory path for uploaded files at runtime.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    today = datetime.now().strftime('%Y-%m-%d')
    return os.path.join('attachments', today, filename)


class Post(models.Model):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
    )

    body = models.TextField(
        verbose_name=_('content body'),
    )

    created = models.DateTimeField(
        verbose_name=_('created time'),
        auto_now_add=True,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('author'),
        related_name='posts',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk, ])


class Attachment(AbstractAttachment):
    file = models.FileField(
        verbose_name=_('uploaded file'),
        upload_to=upload_directory_path,
        storage=default_storage,
    )

    post = models.ForeignKey(
        'Post',
        verbose_name=_('post'),
        related_name='attachments',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
