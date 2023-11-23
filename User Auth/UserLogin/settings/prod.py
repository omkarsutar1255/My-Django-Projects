from .base import *

ALLOWED_HOSTS = ['websitename.com',]

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'main',
        'USER':'root',
        'PASSWORD':os.getenv('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}