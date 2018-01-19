from django.http import JsonResponse
from django.views.generic.edit import FormView

from .forms import (
    UploadAttachmentForm, DeleteAttachmentForm
)


class FileUploadView(FormView):
    form_class = UploadAttachmentForm

    def upload_files(self, *args, **kwargs):
        return None

    def form_valid(self, form):
        files = self.upload_files(uploaded_files=self.request.FILES)
        data = {"files": files}
        return JsonResponse(data)

    def form_invalid(self, form):
        return JsonResponse({
            'status': 'false',
            'message': 'Bad Request'
        }, status=400)


class FileDeleteView(FormView):
    form_class = DeleteAttachmentForm

    def get_model_instance(self, *args, **kwargs):
        return None

    def form_valid(self, form):
        data = {}
        attachment = self.get_model_instance(file_pk=form.cleaned_data['file_pk'])
        attachment.delete()
        return JsonResponse(data)

    def form_invalid(self, form):
        print(form)
        return JsonResponse({
            'status': 'false',
            'message': 'Bad Request'
        }, status=400)
