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

ALLOWED_HOSTS = ['51.20.98.208', 'localhost', '127.0.0.1','api.caplock.in','15.207.248.77']


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "home",
    "about",
    "services",
    "contact",
    "our_customer",
    "gallery",
    "environment",
    'media_events',
    'infrastructure',
    'corsheaders',
    "nested_admin",
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
    "https://lakevictoria.vercel.app",
    "https://api.caplock.in"
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
    # Home App Models
    "home": "fas fa-home",  # App-level icon for Home
    "home.herosection": "fas fa-image",  # Hero Section
    "home.service": "fas fa-boxes",  # Services
    "home.whychooseusreason": "fas fa-check-circle",  # Why Choose Us
    "home.infrastructuresection": "fas fa-industry",  # Infrastructure
    "home.clientpage": "fas fa-handshake",  # Client Page
    "home.clientlogo": "fas fa-building",  # Client Logo
            # About App
    "about.aboutmain": "fas fa-info-circle",
    "about.aboutcompanymain": "fas fa-building",
    "about.environmentalpage": "fas fa-leaf",
    "about.milestonepage": "fas fa-road",
    "about.visionmissionpage": "fas fa-eye",
    "about.investmentpage": "fas fa-chart-line",
    "about.safetypolicypage": "fas fa-shield-alt",
    "about.managementteampage": "fas fa-users",
    "services.servicemainpage": "fas fa-concierge-bell",
    "services.logisticservicepage": "fas fa-truck",
    "services.serviceareapage": "fas fa-map-marked-alt",
    "services.storageservicepage": "fas fa-warehouse",
    "contact.contactmessage": "fas fa-envelope",
"contact.companycontactinfo": "fas fa-address-card",
 "our_customer.customermainpage": "fas fa-handshake",
 "gallery.gallerypage": "fas fa-images",
 "environment.environmentalpage": "fas fa-leaf",
 "environment.carbonfootprintpage": "fas fa-leaf",
 "environment.oilmanagementpage": "fas fa-oil-can",
  "media_events.mediaeventspage": "fas fa-bullhorn",               
  "media_events.mediaarticle": "fas fa-newspaper",          
  "media_events.event": "fas fa-calendar-alt",             

  "infrastructure.automationpage": "fas fa-robot",               
  "infrastructure.firepage": "fas fa-fire-extinguisher",        
  "infrastructure.powerpage": "fas fa-bolt",                    
  "infrastructure.storagepage": "fas fa-oil-can",               
  "infrastructure.truckloadingpage": "fas fa-truck-loading",    
  "infrastructure.vesselpage": "fas fa-ship"      

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
