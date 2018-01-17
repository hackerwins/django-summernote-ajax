from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from django_summernote_ajax.models import AbstractAttachment


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

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk, ])


class Attachment(AbstractAttachment):
    post = models.ForeignKey(
        'Post',
        verbose_name=_('post'),
        related_name='attachments',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
