from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

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
    attachments = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    def clean_attachments(self):
        data = self.data.getlist('attachments')

        if not data and not all(isinstance(item, int) for item in data):
            raise forms.ValidationError("PK must be integers.")

        return data


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'body': SummernoteWidget(wrapper_class='summernote-wrapper-fixed'),
        }
        fields = '__all__'
