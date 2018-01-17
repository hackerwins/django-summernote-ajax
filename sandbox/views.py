from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView
)
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)

from django_summernote_ajax.views import FileUploadView
from .forms import (
    PostForm, PostAttachmentForm
)
from .models import (
    Attachment, Post
)


class PostFileUploadView(FileUploadView):
    def get_object(self, queryset=None):
        return Attachment()


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'sandbox/post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'sandbox/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'sandbox/post_create.html'

    def get_form_class(self):
        if self.request.method == 'POST':
            # Hidden fields for attachments must be validated.
            return PostAttachmentForm
        else:
            # Hidden fields and file input are not prepopulated but appended to form by AJAX.
            return PostForm

    def form_valid(self, form):
        response = super().form_valid(form)

        # Attachments are not related to any post yet.
        attachments = Attachment.objects.filter(
            pk__in=form.cleaned_data['attachments'],
            post__isnull=True,
        )
        self.object.attachments.set(attachments)
        return response


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'sandbox/post_update.html'

    def get_form_class(self):
        if self.request.method == 'POST':
            # Hidden fields for attachments must be validated.
            return PostAttachmentForm
        else:
            # Hidden fields and file input are not prepopulated but appended to form by AJAX.
            return PostForm


class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'sandbox/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
