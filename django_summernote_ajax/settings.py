from django.conf import settings

# The content-type header uploaded with the file (e.g. text/plain or application/pdf)
DSA_CONTENT_TYPES = getattr(settings, 'DSA_CONTENT_TYPES', ['image', 'video'])

# The allowed file extensions
DSA_FILE_EXTENSIONS = getattr(settings, 'DSA_FILE_EXTENSIONS', ['jpg', 'jpeg', 'gif', 'png'])

# The size, in bytes, of the uploaded file (default: 2MB)
DSA_MAX_UPLOAD_SIZE = getattr(settings, 'DSA_MAX_UPLOAD_SIZE', 2097152)
