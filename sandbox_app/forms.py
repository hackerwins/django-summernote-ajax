from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from django_summernote_ajax import settings as django_summernote_ajax_settings
from . import settings as sandbox_app_settings
from .models import Post
from .widgets import (
    PostSummernoteBs4Widget, PostAdminSummernoteLiteWidget
)


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_group_wrapper_class = 'row'
        self.helper.label_class = 'col-2 col-form-label'
        self.helper.field_class = 'col-10'
        self.helper.include_media = False
        self.helper.add_input(Submit('submit', 'Write'))

    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'body': PostSummernoteBs4Widget(
                options={
                    'upload_url': settings.POST_FILE_UPLOAD_URL,
                    'delete_url': settings.POST_FILE_DELETE_URL,
                    'max_file_count': settings.POST_MAX_FILE_COUNT,
                    'max_upload_size': django_summernote_ajax_settings.DSA_MAX_UPLOAD_SIZE,
                    'content_types': django_summernote_ajax_settings.DSA_CONTENT_TYPES,
                    'file_extensions': django_summernote_ajax_settings.DSA_FILE_EXTENSIONS,
                }
            ),
        }


class PostAttachmentForm(PostForm):
    attachments = forms.UUIDField(widget=forms.HiddenInput(), required=False)

    def clean_attachments(self):
        data = self.data.getlist('attachments')

        count = self.instance.attachments.count() if self.instance else 0

        if count + len(data) > sandbox_app_settings.POST_MAX_FILE_COUNT:
            raise forms.ValidationError(_('Maximum number of files exceeded.'))

        return data


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'body': PostAdminSummernoteLiteWidget(wrapper_class='summernote-wrapper-fixed'),
        }
