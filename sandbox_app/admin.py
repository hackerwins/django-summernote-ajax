from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter

from . import settings as sandbox_app_settings
from .forms import PostAdminForm
from .models import (
    Attachment, Post
)


class NullFilterSpec(SimpleListFilter):
    title = ''
    parameter_name = ''

    def lookups(self, request, model_admin):
        return (
            ('1', 'Has post',),
            ('0', 'No post',),
        )

    def queryset(self, request, queryset):
        kwargs = {
            '%s' % self.parameter_name: None,
        }
        if self.value() == '0':
            return queryset.filter(**kwargs)
        if self.value() == '1':
            return queryset.exclude(**kwargs)
        return queryset


class PostNullFilterSpec(NullFilterSpec):
    title = 'post'
    parameter_name = 'post'


class AttachmentInline(admin.StackedInline):
    model = Attachment
    extra = 2
    max_num = sandbox_app_settings.POST_MAX_FILE_COUNT


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'file', 'created')
    list_filter = (PostNullFilterSpec,)
    ordering = ('-created',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    form = PostAdminForm
    inlines = [AttachmentInline]
    ordering = ('-created',)

    class Media:
        js = (
            # django admin jQuery is not compatible with summernote.
            '//ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js',
        )


admin.site.register(Post, PostAdmin)
admin.site.register(Attachment, AttachmentAdmin)
