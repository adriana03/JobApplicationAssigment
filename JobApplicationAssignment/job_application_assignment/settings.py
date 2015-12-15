"""
Django settings for JobApplicationAssignment project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

SETTINGS_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, os.pardir))
STATIC_NAME = "static"
STATIC_DIR = "/".join([STATIC_NAME])
STATIC_DOC_ROOT = os.path.join(SETTINGS_DIR, STATIC_NAME)

import sys
sys.path.insert(0, PROJECT_DIR)





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v@g@)lc)9(x&j_4d+42lnu95w+-rvw$v7d_c3tjhifuezz99!('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTHENTICATION_BACKENDS = (
   
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
  
)



# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bynder',
    'allauth',
    'allauth.account',
    'django.contrib.admindocs',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'job_application_assignment.middlewares.RequireLoginMiddleware',

)

SITE_ID = 1
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = 'index'

LOGIN_REQUIRED_URLS = (
    r'/(.*)$',
)
LOGIN_REQUIRED_URLS_EXCEPTIONS = (
    r'(.*)/admin(.*)$',
    r'(.*)/login(.*)$',
    r'(.*)/logout(.*)$',
    r'(.*)/i18n/setlang/(.*)$',
    r'(.*)/signup(.*)$',
    r'(.*)/accounts/password/reset(.*)$',
    r'(.*)/accounts/confirm-email/(.*)$',
)
ROOT_URLCONF = 'job_application_assignment.urls'



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

TEMPLATE_CONTEXT_PROCESSORS = (
  
    "django.core.context_processors.request",
    'django.contrib.auth.context_processors.auth',
    'allauth.account.context_processors.account',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SETTINGS_DIR, 'templates'),
)

WSGI_APPLICATION = 'job_application_assignment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # :DEPLOY
        'NAME': 'Bynder',
        # :DEPLOY
        'USER': 'root',
        # :DEPLOY
        'PASSWORD': 'root',
    }
}


ACCOUNT_AUTHENTICATION_METHOD = ("username")
#
# Twitter oAuth does not send the email address. See
# https://twittercommunity.com/t/how-to-get-email-from-twitter-user-using-oauthtokens/558
# 
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = ("mandatory")
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
