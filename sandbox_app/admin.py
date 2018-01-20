from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter

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


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'file', 'created')
    list_filter = (PostNullFilterSpec,)
    ordering = ('-created',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    form = PostAdminForm
    inlines = [AttachmentInline]
    ordering = ('-created',)


admin.site.register(Post, PostAdmin)
admin.site.register(Attachment, AttachmentAdmin)
