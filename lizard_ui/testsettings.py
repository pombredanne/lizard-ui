import os

DEBUG = True
TEMPLATE_DEBUG = True
DATABASES = {
    'default': {'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'test.db'},
    }
SITE_ID = 1
INSTALLED_APPS = [
    'lizard_ui',
    'compressor',
    'south',
    'django_extensions',
    'django_nose',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    ]
ROOT_URLCONF = 'lizard_ui.urls'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Note: the below settings are more elaborate than needed,
# but we want to test django_compressor's compressing which
# needs a media url and root and so.

# Set COMPRESS to True if you want to test compression when
# DEBUG == True.  (By default, COMPRESS is the opposite of
# DEBUG).
COMPRESS = False

# SETTINGS_DIR allows media paths and so to be relative to
# this settings file instead of hardcoded to
# c:\only\on\my\computer.
SETTINGS_DIR = os.path.dirname(os.path.realpath(__file__))

# BUILDOUT_DIR is for access to the "surrounding" buildout,
# for instance for BUILDOUT_DIR/var/static files to give
# django-staticfiles a proper place to place all collected
# static files.
BUILDOUT_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, '..'))

# Absolute path to the directory that holds user-uploaded
# media.
MEDIA_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'media')
# Absolute path to the directory where django-staticfiles'
# "bin/django build_static" places all collected static
# files from all applications' /media directory.
STATIC_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'static')

# URL that handles the media served from MEDIA_ROOT. Make
# sure to use a trailing slash if there is a path component
# (optional in other cases).
MEDIA_URL = '/media/'
# URL for the per-application /media static files collected
# by django-staticfiles.  Use it in templates like "{{
# MEDIA_URL }}mypackage/my.css".
STATIC_URL = '/static_media/'
# URL prefix for admin media -- CSS, JavaScript and
# images. Make sure to use a trailing slash.  Uses
# STATIC_URL as django-staticfiles nicely collects admin's
# static media into STATIC_ROOT/admin.
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # Enable support for django-compressor.
    'compressor.finders.CompressorFinder',
    # Enable 'old' /media directories in addition to /static.
    'staticfiles.finders.LegacyAppDirectoriesFinder',
    )
