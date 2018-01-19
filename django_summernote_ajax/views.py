from django.http import JsonResponse
from django.views.generic.edit import FormView

from .forms import (
    UploadAttachmentForm, DeleteAttachmentForm
)


class FileUploadView(FormView):
    form_class = UploadAttachmentForm

    def get_model_instance(self, *args, **kwargs):
        return None

    def form_valid(self, form):
        files = []

        for file in self.request.FILES.getlist('files'):
            attachment = self.get_model_instance()

            attachment.file = file
            attachment.name = file.name

            # TODO: **kwargs?
            attachment.save()

            files.append({
                "pk": attachment.pk,
                "name": file.name,
                "size": file.size,
                "url": attachment.file.url
            })

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
