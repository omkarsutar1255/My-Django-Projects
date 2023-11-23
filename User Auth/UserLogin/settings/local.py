from .base import *

ALLOWED_HOSTS = ['localhost', 'www.example.com', '127.0.0.1']
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'standard':{
            'format':'{asctime} - {levelname} - {name} - {message}',
            'style': "{"
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',

        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'CRUD.log',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'main': {
            'handlers':['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        }
    },
}
