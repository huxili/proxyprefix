DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'fake_secret'

ROOT_URLCONF = 'tests.fake_app.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'irrelevant.db'
    }
}

MIDDLEWARE_CLASSES = []

INSTALLED_APPS = (
    'proxyprefix',
)

STATIC_ROOT = ''
STATIC_URL = '/'

APPEND_SLASH = False