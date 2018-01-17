from django.contrib import admin

from .forms import PostAdminForm
from .models import (
    Attachment, Post
)


class AttachmentInline(admin.StackedInline):
    model = Attachment
    extra = 2


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'file', 'created')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    form = PostAdminForm
    inlines = [AttachmentInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Attachment, AttachmentAdmin)
