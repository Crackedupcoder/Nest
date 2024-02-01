from .base import *
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = [
    ('Ibrahim Abdulsamad', 'ibrahimabduldamad911@gmail.com'),
]

DATABASES = {
'default': {
}
}

database_url = env('DATABASE_URL')
DATABASES['default'] = dj_database_url.parse(database_url)

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
# AWS_PRIVATE_BUCKET_NAME applies to s3-example-public-and-private only
AWS_STORAGE_BUCKET_NAME = 'Futmx-Lodge'
AWS_PRIVATE_BUCKET_NAME = 'Futmx-Lodge'
AWS_S3_REGION_NAME = 'us-east-005'
AWS_S3_ENDPOINT_URL = 'https://s3.us-east-005.backblazeb2.com'
AWS_S3_FILE_OVERWRITE = False

DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'futmxlodge@gmail.com'
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True 
SECURE_HSTS_SECONDS = 3600 # new
SECURE_HSTS_INCLUDE_SUBDOMAINS = True # new
SECURE_HSTS_PRELOAD = True # new
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True # new
CSRF_COOKIE_SECURE = True