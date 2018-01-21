from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from django_summernote_ajax.widgets import SummernoteWidget
from .models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_group_wrapper_class = 'row'
        self.helper.label_class = 'col-2 col-form-label'
        self.helper.field_class = 'col-10'
        self.helper.add_input(Submit('submit', 'Write'))

    class Meta:
        model = Post
        fields = ['title', 'body']


class PostAttachmentForm(PostForm):
    attachments = forms.UUIDField(widget=forms.HiddenInput(), required=False)

    def clean_attachments(self):
        data = self.data.getlist('attachments')

        count = self.instance.attachments.count() if self.instance else 0

        if count + len(data) > settings.POST_MAX_FILE_COUNT:
            raise forms.ValidationError(_('Maximum number of files exceeded.'))

        return data


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'body': SummernoteWidget(wrapper_class='summernote-wrapper-fixed'),
        }
        fields = '__all__'
