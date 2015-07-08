import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

ROOT_URLCONF = 'vrin.urls'
WSGI_APPLICATION = 'vrin.wsgi.application'

LANGUAGE_CODE = 'es-PE'
USE_I18N = True
USE_L10N = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]