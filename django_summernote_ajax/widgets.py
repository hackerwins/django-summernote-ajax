from django.forms import widgets
from django.template import loader
from django.utils.safestring import mark_safe


class SummernoteWidgetBase(widgets.Textarea):
    def __init__(self, attrs=None, wrapper_class='', options=''):
        self.wrapper_class = wrapper_class
        self.options = options

        super(SummernoteWidgetBase, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None, renderer=None):
        context = {
            'widget': {
                'name': name,
                'value': value,
                'wrapper_class': self.wrapper_class,
                'options': self.options,
            }
        }

        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)


class SummernoteLiteWidget(SummernoteWidgetBase):
    template_name = 'django_summernote_ajax/django_summernote_ajax_lite.html'

    class Media:
        css = {
            'all': (
                'css/summernote/summernote-lite.css',
                'css/django-summernote.css',
            )
        }
        js = (
            # django admin jQuery is not compatible with summernote.
            'js/summernote/jquery-3.3.1.min.js',
            'js/summernote/summernote-lite.js',
        )


class SummernoteBs3Widget(SummernoteWidgetBase):
    template_name = 'django_summernote_ajax/django_summernote_ajax_bs3.html'

    class Media:
        css = {
            'all': (
                'css/summernote/summernote.css',
            )
        }
        js = (
            'js/summernote/summernote.js',
        )


class SummernoteBs4Widget(SummernoteWidgetBase):
    template_name = 'django_summernote_ajax/django_summernote_ajax_bs4.html'

    class Media:
        css = {
            'all': (
                'css/summernote/summernote-bs4.css',
            )
        }
        js = (
            'js/summernote/summernote-bs4.js',
        )
