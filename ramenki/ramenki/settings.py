"""
Django settings for ramenki project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from easy_thumbnails.conf import Settings as thumbnailSettings  # Image cropping

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=asn27y@5t&lcu943md3=be0x0%$notob+gbbym%d^q2!vzl%s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOCAL = True

ALLOWED_HOSTS = ['localhost', '*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',  # Social auth
    'news.apps.NewsConfig',
    'users.apps.UsersConfig',
    'other.apps.OtherConfig',
    'mediacontent.apps.MediacontentConfig',
    'static_pages.apps.StaticPagesConfig',
    'adminsortable2',  # Django admin drag'n'drop sorting
    'autoslug',  # Auto creating unique urls
    'ckeditor',  # Text editor
    'ckeditor_uploader',  # Uploading images text editor
    'easy_thumbnails',  # Image cropping
    'image_cropping',  # Image cropping
    'multiselectfield',  # Multiple choice field
    'django_cleanup.apps.CleanupConfig',  # Auto deletion of unused files files
    'django_user_agents',  # Detecting mobile device
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Image cropping
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnailSettings.THUMBNAIL_PROCESSORS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     },
# }

ROOT_URLCONF = 'ramenki.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ramenki.context_processors.links',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'ramenki.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if LOCAL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    # MySQL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ["DB_NAME"],
            'USER': os.environ["DB_USER"],
            'PASSWORD': os.environ["DB_PASSWORD"],
            'HOST': 'localhost',
            'PORT': '',
            'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# CKEditor
CKEDITOR_UPLOAD_PATH = 'editor/'
CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar': 'full',
        'height': 300,
        'width': "100%",
        'extraPlugins': ','.join([
            'uploadimage',
            'autolink',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
        ]),
        'extraAllowedContent': '*(*)',
        'allowedContent': True,
    },
}


# Email sending
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_HOST = 'localhost'
EMAIL_PORT = 587
EMAIL_HOST_USER = "mail@ramenki.doweed-showcase.ru"
EMAIL_HOST_PASSWORD = "f!3h)vU^P1rj"
DEFAULT_FROM_EMAIL = "mail@ramenki.doweed-showcase.ru"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
MEDIA_URL = '/media-url/'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
if LOCAL:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Auth
LOGIN_URL = 'auth:login'
AUTH_USER_MODEL = 'users.CustomUser'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.odnoklassniki.OdnoklassnikiOAuth2',
)
if not LOCAL:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Social Auth
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_USER_MODEL = 'users.CustomUser'
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ('email', )
SOCIAL_AUTH_RAISE_EXCEPTIONS = True
if not LOCAL:
    SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_KEY = '731339637429144'
SOCIAL_AUTH_FACEBOOK_SECRET = '1434323889571275e4091ac6e416f31d'

SOCIAL_AUTH_VK_OAUTH2_KEY = '7573010'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'V3y4koTqdfVpccKZExPZ'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_VK_OAUTH2_EXTRA_DATA = ['photo_max_orig', 'photo_50', 'has_photo', 'bdate']

SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_KEY = 'CCDEHOJGDIHBABABA'
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_SECRET = '2475A43381BFB0038EE199D0'
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_PUBLIC_NAME = 'ramenki'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/profile/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login/'
SOCIAL_AUTH_LOGIN_URL = '/login/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/login/'
SOCIAL_AUTH_INACTIVE_USER_URL = '/login/'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'users.pipeline.fill_user_profile',
)