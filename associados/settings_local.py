#!/usr/bin/env python
# encoding: utf-8
import sys
from settings import *

DEBUG = True

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASEDIR, 'associados.sqlite')
}

INTERNAL_IPS = ('127.0.0.1',)

# You've installed lessc, right?
COMPRESS_PRECOMPILERS = (
    ('text/less', '/opt/local/lib/node_modules/less/bin/lessc {infile} {outfile}'),
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES.append(
    'debug_toolbar.middleware.DebugToolbarMiddleware'
)

INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS.append(
    'debug_toolbar'
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FILE_PATH = '/tmp/lead-messages'  # change this to a proper location

EMAIL_CONTACT_ADDRESS = 'email@fake.com'

PAGSEGURO['email'] = 'email@fake.com'
PAGSEGURO['token'] = 'faketoken'

#using pagseguro-fake-server: https://github.com/andrewsmedina/pagseguro-fake-server
PAGSEGURO_BASE = 'http://localhost:8889/v2'
PAGSEGURO_CHECKOUT = '%s/checkout' % PAGSEGURO_BASE
PAGSEGURO_TRANSACTIONS = '%s/transactions' % PAGSEGURO_BASE
PAGSEGURO_TRANSACTIONS_NOTIFICATIONS = '%s/notifications' % PAGSEGURO_TRANSACTIONS
PAGSEGURO_WEBCHECKOUT = 'https://pagseguro.uol.com.br/v2/checkout/payment.html?code='


MEDIA_ROOT = os.path.join(BASEDIR, 'media')
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_ROOT = os.path.join(BASEDIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = ()
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_LESS_BINARY = ()
PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
    'pipeline.compilers.stylus.StylusCompiler',
)

COMPRESS_OUTPUT_DIR = 'cache'
