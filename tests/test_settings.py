SECRET_KEY = 'django_summernote_ajax_fake_key'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += [
    'django_summernote_ajax',
    'sandbox_app',
]

ROOT_URLCONF = 'sandbox.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db_test.sqlite3',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# The content-type header uploaded with the file (default: ['image', 'video'])
DSA_CONTENT_TYPES = ['image', 'video']
# The allowed file extensions (default: ['jpg', 'jpeg', 'gif', 'png'])
DSA_FILE_EXTENSIONS = ['jpg', 'jpeg', 'gif', 'png']
# The size, in bytes, of the uploaded file (default: 2MB)
DSA_MAX_UPLOAD_SIZE = 2097152

# The maximum number of uploaded files
POST_MAX_FILE_COUNT = 1

# URLs for file upload and download
POST_FILE_UPLOAD_URL = '/upload-file'
POST_FILE_DELETE_URL = '/delete-file'
