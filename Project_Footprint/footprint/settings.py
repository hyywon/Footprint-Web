"""
Django settings for footprint project.
Generated by 'django-admin startproject' using Django 3.0.8.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w6f3ty@tyocqqav@j(0hc%2+b)sb$3zadp6_2*5lab3_xl8$8r'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']
# Application definition
AUTH_USER_MODEL = 'website.User'
INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'rest_framework',
    'django_filters',
    'rangefilter',
    'rest_registration',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [

    ],
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]    
}

REST_REGISTRATION = {
    'REGISTER_VERIFICATION_ENABLED': True,
    'VERIFICATION_FROM_EMAIL' : 'abc@gmail.com',
    'REGISTER_VERIFICATION_EMAIL_TEMPLATES' : {'subject' : "rest_registration/register/subject.txt", 'html_body' : 'rest_registration/register/body.html'},
    # 'REGISTER_VERIFICATION_EMAIL_TEMPLATES' : {'subject' : '/website/a.txt', 'html_body' : 'rest_registration/register/body.html'},
    'REGISTER_VERIFICATION_URL': ('http://127.0.0.1:8000/api_activate/'),
    'REGISTER_EMAIL_VERIFICATION_ENABLED': False,
    'RESET_PASSWORD_VERIFICATION_ENABLED': False, 
    'USER_LOGIN_FIELDS' :  ['email'],
    'LOGIN_SERIALIZER_CLASS' : ('website.user_serializers.UserLoginSerializer'),
    'SUCCESS_RESPONSE_BUILDER' : ('website.user_serializers.build_default_success_response'),
    # body, subject 내용 바꿀 시에, 새로 venv 다운받을 시 venv/Lib/site-packages/rest_registration/templates/rest_registration/register/ 수정
}
from rest_registration.api.views import login
from rest_registration.api.views import register
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'footprint.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'footprint.wsgi.application'
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'footprintdatabase',
        'USER': 'root',
        'PASSWORD': 's9423093',
        'HOST': 'localhost',
        'PORT': '3306'
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
LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'Asia/Seoul'

# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# for email
AUTHENTICATION_BACKENDS = ['website.backends.EmailAuthBackend']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

## for email verification
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'abc@gmail.com' ## write your Google email : abcd@gmail.com
EMAIL_HOST_PASSWORD = 'aaaa' ## write your email password
EMAIL_USE_TLS = True

#Maintain Session
SESSION_COOKIE_AGE = 60*60
SESSION_SAVE_EVERY_REQUEST = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
