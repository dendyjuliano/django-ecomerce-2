from .base import *

DEBUG = False
ALLOWED_HOSTS = ['ip-address','www.website.com']

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your db_name',
        'USER':'your db_username',
        'PASSWORD':'your db_password',
        'HOST': 'localhost',
        'PORT':''
    }
}

STRIPE_PUBLIC_KEY = 'your public live key'
STRIPE_SECRET_KEY = 'your secreat live key'