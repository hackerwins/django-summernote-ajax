from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    path
)

from sandbox_app.views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostAttachmentUploadView,
    PostAttachmentDeleteView
)

urlpatterns = [
    path('',
         PostListView.as_view(), name='home'),

    path('upload-file',
         PostAttachmentUploadView.as_view(), name='post-file-upload'),

    path('delete-file/<int:pk>',
         PostAttachmentDeleteView.as_view(), name='post-file-delete'),

    path('posts',
         PostListView.as_view(), name='post-list'),

    path('posts/<int:pk>',
         PostDetailView.as_view(), name='post-detail'),

    path('posts/create',
         PostCreateView.as_view(), name='post-create'),

    path('posts/update/<int:pk>',
         PostUpdateView.as_view(), name='post-update'),

    path('posts/delete/<int:pk>',
         PostDeleteView.as_view(), name='post-delete'),

    path('admin/',
         admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
