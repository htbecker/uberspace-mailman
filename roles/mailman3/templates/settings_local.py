# these settings will overwite the values in settings.py
import os

BASE_DIR = '{{ ansible_facts.env.HOME }}/{{ base_dir }}/var/'

SECRET_KEY = '{{ django_secret_key }}'

# Leave to True while debugging, but change to False in production

DEBUG = {{ django_debugging }}
ADMINS = (
     ('{{ django_admin_name }}', '{{ django_admin_email }}'),
)

ALLOWED_HOSTS = [
    "localhost",  # Archiving API from Mailman, keep it.
    # Add here all production URLs you may have.
    "{{ domain }}",
]

# TODO check if local is needed
# TODO check if this port needs chaning
# MAILMAN_REST_API_URL = 'http://isabell.local.uberspace.de:8001'
MAILMAN_REST_API_URL = 'http://{{ domain }}:{{ mailman_port_rest }}'
MAILMAN_REST_API_USER = 'rest_api_admin_user'
MAILMAN_REST_API_PASS = 'rest_api_admin_pw'
MAILMAN_ARCHIVER_KEY = '{{ django_secret_archiver_api_key }}'
MAILMAN_ARCHIVER_FROM = ('0.0.0.0', '::')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # Uncomment
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_SCHEME', 'https') # Uncomment

STATIC_ROOT = '{{ ansible_facts.env.HOME }}/html/static/'

DEFAULT_FROM_EMAIL = '{{ mailbox }}@{{ domain }}'

SERVER_EMAIL = '{{ ansible_facts.env.USER }}@uber.space'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '{{ ansible_facts.fqdn }}'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '{{ mailbox }}@{{ domain }}'
EMAIL_HOST_PASSWORD = '{{ mailbox_pw }}'

COMPRESS_PRECOMPILERS = (
   ('text/less', 'lessc {infile} {outfile}'),
   ('text/x-scss', '{{ ansible_facts.env.HOME }}/bin/dart-sass/sass {infile} {outfile}'),
   ('text/x-sass', '{{ ansible_facts.env.HOME }}/bin/dart-sass/sass {infile} {outfile}'),
)

# Comment the following lines out to test sending mail
if DEBUG == True:
   EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
   EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'emails')
