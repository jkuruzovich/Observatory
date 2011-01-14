import os
import django

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# the login url
LOGIN_URL='/login'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

# Absolute path to the directory that holds cloned repositories.
REPO_ROOT = os.path.join(SITE_ROOT, 'clones')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site-media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Path where screenshots and thumbnails should be placed
SCREENSHOT_PATH = os.path.join(MEDIA_ROOT, 'screenshots')

# Root URL for screenshots
SCREENSHOT_URL = "/site-media/screenshots/"

# The maximum number of threads to use when fetching blogs
BLOG_FETCH_THREAD_COUNT = 10

# The maximum number of concurrent processes to run when fetching repos
REPO_FETCH_PROCESS_COUNT = 4

# The number of minutes before a repository fetch should timeout.
#
# This doesn't apply to the time it takes the clone the repository, just to
# the amount of time it takes to read the logs and generate diffs.
# "Some People" commit massive diffs, other than that this should never be
# an issue unless your computer is very, very slow.
REPO_FETCH_TIMEOUT = 1

# scoring thresholds
GREEN_SCORE = 2880 # everything up to this score will be green
RED_SCORE = 172800 # everything after this score will be red

UNCERTAIN_SCORE = 6000 # everything after this score will be uncertain face
UNHAPPY_SCORE = 86400 # everything after this score will be unhappy face

# the "worst" score allowed, in minutes
MAX_SCORE_MINUTES = 3024000

# use production jquery for production, debug for debug
JQUERY = [os.path.join(MEDIA_URL, "js", "jquery-1.4.4.min.js"),
          os.path.join(MEDIA_URL, "js", "jquery-1.4.4.js")][DEBUG]

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'j+e*h2ket2cf2w##m2fzjp392%68!a^xcjo+_lr_-(^d8c3ea5'

# if True, attempts to use the devserver replacement for runserver in debug
# https://github.com/dcramer/django-devserver
TRY_DEVSERVER = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'observatory.urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates')
)

INSTALLED_APPS = (
    'devserver',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'dashboard',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)

# automatically use devserver if it is available and requested
USE_DEVSERVER = False
if DEBUG and TRY_DEVSERVER:
  try:
    import devserver
    USE_DEVSERVER = True
  except:
    pass

if not USE_DEVSERVER:
  INSTALLED_APPS = INSTALLED_APPS[1:]

DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLSummaryModule',
)