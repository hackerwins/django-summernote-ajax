from django.conf import settings

# The maximum number of uploaded files
POST_MAX_FILE_COUNT = getattr(settings, 'POST_MAX_FILE_COUNT', 10)
