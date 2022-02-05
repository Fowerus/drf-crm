"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# '7q6cym8(r0lgxx_ms5d&$hnz_e@yw0wukcpgfqgx@9f!!!n=^r'
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DJANGO_DEBUG')

# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")


SECRET_KEY = '!!!django-insecure-yo3a4$pt-thta@^b&mpmyk^37)74#(nvgs#q$u5sm!^s5(l1l('
DEBUG = True
ALLOWED_HOSTS = ['62.109.11.4', 'localhost', '127.0.0.1']


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    "EXCEPTION_HANDLER": "core.utils.atomic_exception.crm_exception_handler",
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',

    'corsheaders',
    'rest_framework_simplejwt',
    'rest_framework',
    'django_resized',
    'phonenumber_field',
    'core',
    'Organizations',
    'Users',
    'Clients',
    'Orders',
    'Sessions',
    'VerifyInfo',
    'Market',
    'Handbook',
    'Marketplace',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]


ROOT_URLCONF = 'app.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'HOST': os.environ.get('POSTGRES_HOST'),
    #     'NAME': os.environ.get('POSTGRES_DB'),
    #     'USER': os.environ.get('POSTGRES_USER'),
    #     'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
    #     'PORT': int(os.environ.get('POSTGRES_PORT')),
    # },
    # "mongo": {
    #     "ENGINE": "djongo",
    #     "NAME": os.environ.get('MONGO_DB_NAME'),
    #     "CLIENT": {
    #         "host":  os.environ.get('MONGO_DB_HOST'),
    #         "port": int(os.environ.get('MONGO_DB_PORT')),
    #         "username": os.environ.get('MONGO_DB_USERNAME'),
    #         "password": os.environ.get('MONGO_DB_PASSWORD'),
    #     },
    #     'TEST': {
    #         'MIRROR': 'default',
    #     },
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '',
        'NAME': 'fower',
        'USER': 'fower',
        'PASSWORD': 'fower',
        'PORT': 5432,
    },
    "mongo": {
        "ENGINE": "djongo",
        "NAME": 'mongo',
        'TEST': {
            'MIRROR': 'default',
        },
    }
}

DATABASE_ROUTERS = ['core.utils.db_routers.DataBaseRouter', ]

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators


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

AUTH_USER_MODEL = "Users.User"

# CELERY_TASK_TRACK_STARTED = True
# CELERY_TASK_TIME_LIMIT = 30 * 60
# CELERY_IGNORE_RESULT = True
# CELERY_BROKER_URL = os.environ.get('CELERY_URL')
# CELERY_RESULT_BACKEND = os.environ.get('CELERY_URL')
# CELERYD_HIJACK_ROOT_LOGGER = False
# REDIS_CHANNEL_URL = os.environ.get('REDIS_CHANNEL_URL')

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, 'static')


STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
APPEND_SLASH = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_HOST_USER = 'verify@api-test.go-best.ru'
# EMAIL_HOST_PASSWORD = 'Gobest2021'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# CSRF_COOKIE_DOMAIN = None
# CORS_ALLOW_ALL_ORIGINS = True
# CSRF_COOKIE_DOMAIN = None
# CSRF_TRUSTED_ORIGINS = os.environ.get(
#     "DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")


ACCESS_TOKEN_LIFETIME = 365*24*3600
SMC_CODE_LIFETIME = 60
RESEND_SMS_AFTER = 90

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=ACCESS_TOKEN_LIFETIME),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365),
    # 'ROTATE_REFRESH_TOKENS': False,
    # 'BLACKLIST_AFTER_ROTATION': False,
    # 'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    # 'SIGNING_KEY': SECRET_KEY,
    # 'VERIFYING_KEY': None,
    # 'AUDIENCE': None,
    # 'ISSUER': None,
    # 'JWK_URL': None,
    # 'LEEWAY': 0,

    # 'AUTH_HEADER_TYPES': ('Bearer',),
    # 'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    # 'USER_ID_FIELD': 'id',
    # 'USER_ID_CLAIM': 'user_id',
    # 'USER_AUTHENTICATION_RULE':
    #     'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    # 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # 'TOKEN_TYPE_CLAIM': 'token_type',

    # 'JTI_CLAIM': 'jti',

    # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=15),
    # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
