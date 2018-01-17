from django.forms import widgets
from django.template import loader
from django.utils.safestring import mark_safe


class SummernoteWidget(widgets.Textarea):
    template_name = 'django_summernote_ajax/django_summernote_ajax.html'

    class Media:
        css = {
            'all': (
                'css/summernote/summernote-lite.css',
                'css/django-summernote.css',
            )
        }
        js = (
            'js/summernote/jquery-3.2.1.min.js',  # django admin jQuery is not compatible with summernote.
            'js/summernote/summernote-lite.js',
        )

    def __init__(self, attrs=None, wrapper_class='', options=''):
        self.wrapper_class = wrapper_class
        self.options = options

        super(SummernoteWidget, self).__init__(attrs=attrs)

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
