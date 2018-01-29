import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractAttachment(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('file name'),
    )

    # PK is a private identifier
    uid = models.UUIDField(
        verbose_name=_('public identifier'),
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )

    file = models.FileField(
        verbose_name=_('uploaded file'),
        upload_to="attachments",
    )

    created = models.DateTimeField(
        verbose_name=_('created time'),
        auto_now_add=True,
    )

    class Meta:
        abstract = True
        verbose_name = _('attachment')
        verbose_name_plural = _('attachments')
        ordering = ['-created']

    def __str__(self):
        return self.name
