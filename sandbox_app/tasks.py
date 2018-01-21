from celery import shared_task
from django.core.files.storage import default_storage

from .models import Attachment


@shared_task
def delete_orphan_attachments():
    attachments = Attachment.objects.filter(post__isnull=True)

    count = len(attachments)

    for attachment in attachments:
        default_storage.delete(attachment.file.path)

    attachments.delete()

    return count
