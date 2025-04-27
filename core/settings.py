import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5t-rowu_ta5ekk%_-37jz)j3_%k^6&#rx0zml49f4+oaalb!5b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['51.20.98.208', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "home",
    'corsheaders',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # <-- add this FIRST
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://lakevictoria.vercel.app/",
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (User uploads like images)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
JAZZMIN_SETTINGS = {
    "site_title": "Lake Victoria Logistics Admin",
    "site_header": "Lake Victoria Admin",
    "site_brand": "Lake Victoria",
    "welcome_sign": "Welcome to Lake Victoria Logistics Admin Portal",
    "copyright": "Lake Victoria",

    "search_model": ["auth.User", "website.Customer"],  # Update this as per your models

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "auth"},  # Adds auth section directly in top navbar
        {"app": "website"},  # Add your custom app
    ],

    "usermenu_links": [
        {"name": "Support", "url": "https://lakevictorialogistics.com/contact", "new_window": True}
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    "order_with_respect_to": ["auth", "website"],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "website.Customer": "fas fa-briefcase",
        "website.HomeSection": "fa-solid fa-house",                # Home
        "website.AboutUsSection": "fa-solid fa-address-card",      # About Us
        "website.ServicesSection": "fa-solid fa-briefcase",        # Services
        "website.InfrastructureSection": "fa-solid fa-industry",   # Infrastructure
        "website.EnvironmentSection": "fa-solid fa-leaf",          # Environment
        "website.CustomersSection": "fa-solid fa-users",           # Customers
        "website.MediaSection": "fa-solid fa-photo-film",          # Media & Events
        "website.ImageGallery": "fa-solid fa-image",               # Image Gallery
        "website.ContactUsSection": "fa-solid fa-envelope", 
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # Login page branding
    "login_logo": None,
    "login_logo_dark": None,

    # Color Scheme
    "theme": "minty",  # Try others like 'darkly', 'flatly', 'cyborg', 'superhero', 'lux', 'cosmo'
    "dark_mode_theme": None,

    "custom_css": None,
    "custom_js": None,

    # Change default text on the admin login page
    "changeform_format": "horizontal_tabs",
}
