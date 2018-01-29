from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from sandbox_app.views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostAttachmentUploadView,
    PostAttachmentDeleteView
)

urlpatterns = [
    url(r'^$',
        PostListView.as_view(), name='home'),

    url(r'^upload-file/$',
        PostAttachmentUploadView.as_view(), name='post-file-upload'),

    url(r'^delete-file/$',
        PostAttachmentDeleteView.as_view(), name='post-file-delete'),

    url(r'^posts/$',
        PostListView.as_view(), name='post-list'),

    url(r'^posts/(?P<pk>\d+)/$',
        PostDetailView.as_view(), name='post-detail'),

    url(r'^posts/create/$',
        PostCreateView.as_view(), name='post-create'),

    url(r'^posts/update/(?P<pk>\d+)/$',
        PostUpdateView.as_view(), name='post-update'),

    url(r'^posts/delete/(?P<pk>\d+)/$',
        PostDeleteView.as_view(), name='post-delete'),

    url(r'^admin/',
        admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
