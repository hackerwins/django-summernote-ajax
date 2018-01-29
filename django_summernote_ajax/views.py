from django.http import JsonResponse
from django.views.generic.edit import FormView

from .forms import (
    UploadAttachmentForm, DeleteAttachmentForm
)


class FileUploadView(FormView):
    """Provide a way to show and handle uploaded files in a request."""
    form_class = UploadAttachmentForm

    def upload_file(self, *args, **kwargs):
        """Abstract method must be overridden."""
        raise NotImplementedError

    def form_valid(self, form):
        """If the form is valid, return JSON file list after saving them"""
        data = self.upload_file(uploaded_files=self.request.FILES)
        return JsonResponse(data)

    def form_invalid(self, form):
        """If the form is invalid, return HTTP 400 error"""
        return JsonResponse({
            'status': 'false',
            'message': 'Bad Request'
        }, status=400)


class FileDeleteView(FormView):
    """Provide a way to show and handle files to be deleted in a request."""
    form_class = DeleteAttachmentForm

    def delete_file(self, *args, **kwargs):
        """Abstract method must be overridden."""
        raise NotImplementedError

    def form_valid(self, form):
        """If the form is valid, return JSON file list after deleting them"""
        data = self.delete_file(form=form, user=self.request.user)
        return JsonResponse(data)

    def form_invalid(self, form):
        """If the form is invalid, return HTTP 400 error"""
        return JsonResponse({
            'status': 'false',
            'message': 'Bad Request'
        }, status=400)
