from django.http import JsonResponse
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView

from .forms import (
    UploadAttachmentForm, DeleteAttachmentForm
)


class FileUploadView(SingleObjectMixin, FormView):
    form_class = UploadAttachmentForm

    def form_valid(self, form):
        files = []

        for file in self.request.FILES.getlist('files'):
            # TODO: dynamically retrieve instance?
            attachment = self.get_object()

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


class FileDeleteView(SingleObjectMixin, FormView):
    form_class = DeleteAttachmentForm

    def form_valid(self, form):
        data = {}
        # TODO: How to retrieve object?

        return JsonResponse(data)

    def form_invalid(self, form):
        return JsonResponse({
            'status': 'false',
            'message': 'Bad Request'
        }, status=400)
