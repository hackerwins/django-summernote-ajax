from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractAttachment(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('file name'),
    )

    file = models.FileField(
        verbose_name=_('uploaded file'),
        upload_to="attachment",
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
