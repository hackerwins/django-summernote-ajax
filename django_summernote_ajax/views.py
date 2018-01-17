from django.http import JsonResponse
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin

from .forms import AttachmentForm


class FileUploadView(FormMixin, SingleObjectMixin, View):
    form_class = AttachmentForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        files = []

        if form.is_valid():
            for file in request.FILES.getlist('files'):
                attachment = self.get_object()

                attachment.file = file
                attachment.name = file.name
                attachment.save(**kwargs)

                files.append({
                    "pk": attachment.pk,
                    "name": file.name,
                    "size": file.size,
                    "url": attachment.file.url
                })

            data = {"files": files}

            return JsonResponse(data)
        else:
            return JsonResponse({
                'status': 'false',
                'message': 'Bad Request'
            }, status=400)
