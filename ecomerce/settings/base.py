import moneyed
from pathlib import Path
from decouple import config
from moneyed.localization import _FORMATTER
from decimal import ROUND_HALF_EVEN

BASE_DIR = Path(__file__).resolve().resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'crispy_forms',

    'djmoney',

    'django_filters',

    'cart',

    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecomerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processor.cart_total_amount',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecomerce.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# DJANGO ALLAUTH
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# CRISPY FORM
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = '/'

# ADD NEW CURENCY
IDN = moneyed.add_currency(
    code='IDN',
    numeric='068',
    name='Rupiah',
    countries=('INDONESIA', )
)

_FORMATTER.add_sign_definition(
    'default',
    IDN,
    prefix=u'Bs. '
)

_FORMATTER.add_formatting_definition(
    'es_BO',
    group_size=3, group_separator=".", decimal_point=",",
    positive_sign="",  trailing_positive_sign="",
    negative_sign="-", trailing_negative_sign="",
    rounding_method=ROUND_HALF_EVEN
)

CURRENCIES = ('USD', 'IDN')
CURRENCY_CHOICES = [('USD', 'USD $'), ('IDN', 'IDN Rp')]

#FOR CART
CART_SESSION_ID = 'cart'
