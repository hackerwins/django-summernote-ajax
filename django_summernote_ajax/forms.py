from os.path import splitext

from django import forms
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _


class AttachmentForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True}), required=False)

    def clean_files(self):
        content = self.cleaned_data['files']
        content_type = content.content_type.split('/')[0]
        extension = splitext(content.name)[1][1:].lower()

        if extension not in settings.DSA_FILE_EXTENSIONS \
                or content_type not in settings.DSA_CONTENT_TYPES:
            raise forms.ValidationError(_('File type is not supported'))

        if content.size > settings.DSA_MAX_UPLOAD_SIZE:
            raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
                filesizeformat(settings.DSA_MAX_UPLOAD_SIZE), filesizeformat(content.size)))

        return content
