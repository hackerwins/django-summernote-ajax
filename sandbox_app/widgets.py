from django_summernote_ajax.widgets import (
    SummernoteBs4Widget, SummernoteLiteWidget
)


class PostSummernoteBs4Widget(SummernoteBs4Widget):
    class Media:
        js = (
            'js/post-summernote-ajax.js',
        )


class PostAdminSummernoteLiteWidget(SummernoteLiteWidget):
    class Media:
        css = {
            'all': (
                'css/django-summernote.css',
            )
        }
        js = (
            'js/post-admin-summernote-ajax.js',
        )
