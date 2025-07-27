import os
from pathlib import Path

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-strong-secret-key-here'

DEBUG = False  # For local development only

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# ==============================================
#               INSTALLED APPS
# ==============================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'relationship_app',
    'bookshelf',
    'csp',  # 👈 Added Content Security Policy app
]

AUTH_USER_MODEL = 'bookshelf.CustomUser'

# ==============================================
#               MIDDLEWARE
# ==============================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',  # 👈 Added here
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==============================================
#         CONTENT SECURITY POLICY (CSP)
# ==============================================
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", 'https://fonts.googleapis.com')
CSP_FONT_SRC = ("'self'", 'https://fonts.gstatic.com')
CSP_SCRIPT_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'", 'data:')
CSP_OBJECT_SRC = ("'none'",)

# ==============================================
#         OTHER SECURITY HEADERS
# ==============================================
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ==============================================
#               ROOT URL
# ==============================================
ROOT_URLCONF = 'LibraryProject.urls'

# ==============================================
#               TEMPLATES
# ==============================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'relationship_app', 'templates')],
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

# ==============================================
#               WSGI APPLICATION
# ==============================================
WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# ==============================================
#               DATABASE
# ==============================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==============================================
#               PASSWORD VALIDATION
# ==============================================
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

# ==============================================
#               INTERNATIONALIZATION
# ==============================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==============================================
#               STATIC FILES
# ==============================================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'relationship_app', 'static')
]

# ==============================================
#           LOGIN / LOGOUT CONFIG
# ==============================================
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_URL = '/login/'

# ==============================================
#               DEFAULT PRIMARY KEY
# ==============================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
