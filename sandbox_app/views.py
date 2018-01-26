from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView
)
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)

from django_summernote_ajax.views import (
    FileUploadView, FileDeleteView
)
from .forms import (
    PostForm, PostAttachmentForm
)
from .models import (
    Attachment, Post
)
from .viewmixins import AuthorRequiredMixin


class PostAttachmentUploadView(LoginRequiredMixin, FileUploadView):
    # Raise PermissionDenied exception instead of the redirect
    raise_exception = True

    def upload_file(self, *args, **kwargs):
        """
        This method must be overridden to perform uploading files and return JSON file list.
        """
        uploaded_files = kwargs.pop('uploaded_files', None)
        files = []

        if uploaded_files:
            # NOTE: Change HTML attribute name - `files`
            for file in uploaded_files.getlist('files'):
                # NOTE: Attachment class must inherit AbstractAttachment
                attachment = Attachment()
                attachment.file = file
                attachment.name = file.name
                attachment.save()

                files.append({
                    "uid": attachment.uid,
                    "name": file.name,
                    "size": file.size,
                    "url": attachment.file.url
                })

        # NOTE: Change JSON key name - `files`
        return {"files": files}


class PostAttachmentDeleteView(LoginRequiredMixin, FileDeleteView):
    # Raise PermissionDenied exception instead of the redirect
    raise_exception = True

    def delete_file(self, *args, **kwargs):
        """
        This method must be overridden to perform deleting files and return JSON file list.
        """
        form = kwargs.pop('form', None)
        user = kwargs.pop('user', None)

        files = []

        if form and user:
            # NOTE: Attachment class must inherit AbstractAttachment and asynchronously deleted by cron.
            attachment = Attachment.objects.select_related('post__author').get(uid=form.cleaned_data['uid'])

            if attachment.post and attachment.post.author == user:
                attachment.post = None
                attachment.save()

            files.append({
                "uid": attachment.uid,
            })

        # NOTE: Change JSON key name - `files`
        return {"files": files}


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'sandbox_app/post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'sandbox_app/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'sandbox_app/post_create.html'
    login_url = '/admin/login'
    redirect_field_name = '/admin'

    def get_form_class(self):
        """
        Return different form when validation is required.
        Hidden fields are not prepopulated but appended to form by AJAX.
        """
        if self.request.method == 'POST':
            return PostAttachmentForm
        else:
            return PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user

        # NOTE: Author has to be set before `form_valid()` which saves Post model instance.
        # Then, `self.object` is available in order to save attachments.
        response = super().form_valid(form)

        # Retrieve attachments not related to any post yet.
        attachments = Attachment.objects.filter(
            uid__in=form.cleaned_data['attachments'],
            post__isnull=True,
        )

        if attachments:
            self.object.attachments.set(attachments)

        return response


class PostUpdateView(AuthorRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'sandbox_app/post_update.html'
    login_url = '/admin/login'
    redirect_field_name = '/admin'

    def get_form_class(self):
        """
        Return different form when validation is required.
        Hidden fields are not prepopulated but appended to form by AJAX.
        """
        if self.request.method == 'POST':
            return PostAttachmentForm
        else:
            return PostForm

    def form_valid(self, form):
        response = super().form_valid(form)

        # Retrieve attachments not related to any post yet.
        attachments = Attachment.objects.filter(
            uid__in=form.cleaned_data['attachments'],
            post__isnull=True,
        )

        if attachments:
            attachments.update(post=self.object)

        return response


class PostDeleteView(AuthorRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'sandbox_app/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    login_url = '/admin/login'
    redirect_field_name = '/admin'
