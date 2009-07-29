# Django settings for meu_blog project.

# Criado por mim Andre Ventura
import os
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


# DEBUG = True <==== Alterado por mim para uso do local_settings.py
LOCAL = False # Criado por mim - pag 172 - vol 1
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
# DATABASE_NAME = '/home/ventura/django_segundo_projeto/meu_blog/meu_blog.db'  # Or path to database file if using sqlite3.
DATABASE_NAME =  os.path.join(PROJECT_ROOT_PATH,'meu_blog.db')                 # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Criado por mim Andre Ventura
try:
    from local_settings import *
except ImportError:
    pass


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
# Caminho deve ser indicado em urls.py <============= Andre Ventura
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'x4cd--l=4d))sya9$%d&&$9ay7o3gd%br4gsf-=$vuqcid_@&3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#   'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

# ROOT_URLCONF = 'meu_blog.urls' Retirado por mim - PYTHONPATH - pag 174 - vol 1 
ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    
    # 'templates', <--- Retirado por mim e substituido pelo abaixo. OBS: Verificar acima o import no comeco deste arquivo 
    os.path.join(PROJECT_ROOT_PATH,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.syndication',
    'django.contrib.flatpages',
    'django.contrib.comments',
    'meu_blog.blog',
    'meu_blog.galeria',
    )

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ventura11@gmail.com'
EMAIL_HOST_PASSWORD = '172349av'
EMAIL_SUBJECT_PREFIX = '[Blog do Alatazan]'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
