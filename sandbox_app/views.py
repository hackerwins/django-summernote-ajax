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


class PostAttachmentUploadView(FileUploadView):
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
                    "pk": attachment.pk,
                    "name": file.name,
                    "size": file.size,
                    "url": attachment.file.url
                })

        # NOTE: Change JSON key name - `files`
        return {"files": files}


class PostAttachmentDeleteView(FileDeleteView):
    def delete_file(self, *args, **kwargs):
        """
        This method must be overridden to perform deleting files and return JSON file list.
        """
        form = kwargs.pop('form', None)

        files = []

        if form:
            # NOTE: Change POST form data name - `file_pk`
            # NOTE: Attachment class must inherit AbstractAttachment.
            attachment = Attachment.objects.get(pk=form.cleaned_data['file_pk'])

            # NOTE: Attachment must be asynchronously deleted by cron.
            attachment.post = None
            attachment.save()

            files.append({
                "pk": attachment.pk,
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


class PostCreateView(CreateView):
    model = Post
    template_name = 'sandbox_app/post_create.html'

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

        # Attachments are not related to any post yet.
        attachments = Attachment.objects.filter(
            pk__in=form.cleaned_data['attachments'],
            post__isnull=True,
        )

        if attachments:
            self.object.attachments.set(attachments)

        return response


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'sandbox_app/post_update.html'

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

        # Attachments are not related to any post yet.
        attachments = Attachment.objects.filter(
            pk__in=form.cleaned_data['attachments'],
            post__isnull=True,
        )

        if attachments:
            attachments.update(post=self.object)

        return response


class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'sandbox_app/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
