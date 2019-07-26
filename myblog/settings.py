"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

import pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bpv59-0*vv^%e#g838jo4)p$g+7oe6to72nd3=6!m6w2gquhmn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
# �������������
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog1',
    'tinymce',
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

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'blog1/templates','blog1/static')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
                        'blog_tags': 'blog1.static.templatetags.blog_tags',
                        }
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

'''
DATABASES = {
      'default': {
      'ENGINE': 'django.db.backends.mysql',
     'NAME':'blog',
     'USER': 'root',
      'PASSWORD': 'lingl.',
      'HOST': '47.106.79.122',
      'PORT': '3306',
      }
 }

'''




# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
'''
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static')
STATICFILES_DIRS = (
('css',os.path.join(STATIC_ROOT,'css').replace('\\','/') ),
('js',os.path.join(STATIC_ROOT,'js').replace('\\','/') ),
('images',os.path.join(STATIC_ROOT,'images').replace('\\','/') ),
('upload',os.path.join(STATIC_ROOT,'upload').replace('\\','/') ),
)
'''


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'blog1/'
                           'static'),
    ]
TINYMCE_DEFAULT_CONFIG = {
      # // General options
     'mode': 'textareas',
      'theme': "advanced",
      'plugins': "pagebreak,prettify,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,"
                 "insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,wordcount,advlist,autosave",

      # // Theme  options
      'theme_advanced_buttons1': "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect,fullscreen,code",
      'theme_advanced_buttons2': "cut,copy,paste,pastetext,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,|,insertdate,inserttime,preview,|,forecolor,backcolor",
     'theme_advanced_buttons3': "tablecontrols,|,hr,removeformat,prettify,visualaid,|,sub,sup,|,charmap,emotions,"
                                "iespell,media,advhr,|,print,|,ltr,rtl",
     'theme_advanced_toolbar_location': "top",
     'theme_advanced_toolbar_align': "left",
     'theme_advanced_statusbar_location': "bottom",
     'theme_advanced_resizing': 'true',

     # // content_css: "/css/style.css",
     'template_external_list_url': "lists/template_list.js",
     'external_link_list_url': "lists/link_list.js",
     'external_image_list_url': "lists/image_list.js",
     'media_external_list_url': "lists/media_list.js",

 # // Style formats
     'style_formats': [
     {'title': 'Bold text', 'inline': 'strong'},
     {'title': 'Red text', 'inline': 'span', 'styles': {'color': '#ff0000'}},
     {'title': 'Help', 'inline': 'strong', 'classes': 'help'},
     {'title': 'Table styles'},
     {'title': 'Table row 1', 'selector': 'tr', 'classes': 'tablerow'}
     ],
     'width': '400',
     'height': '300'
 }