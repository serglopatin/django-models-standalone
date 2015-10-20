import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '{{ secret_key }}'

# WARNING: when DEBUG is True, don't forget to reset db connection to avoid memory leaks in your standalone app!
DEBUG = True

INSTALLED_APPS = (
        "models_standalone",
)

MIDDLEWARE_CLASSES = []

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True