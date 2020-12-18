"""
Django settings for superDream project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's#bh_k6xgkkal@-k_u*&$!$uur4+p3k60#h7%m@@qyv3m6ih#o'

# SECURITY WARNING: don't run with debug turned on in production!
# You must have your ALLOWED_HOSTS set up correctly when you set this
# DEBUG = False, or you get a 404 error.
DEBUG = False


# The second one here will not load even if DEBUG = True.
ALLOWED_HOSTS = ['www.thehyperdream.com', 'https://thehyperDream.com',
                'https://www.thehyperDream.com', 'thehyperdream.com',
                'http://thehyperdream.com', 'http://www.thehyperdream.com']

# Local
#ALLOWED_HOSTS = []


# Application definition

#PAYPAL_TEST = True

INSTALLED_APPS = [

    'myDream',   # This works on local and production.
    'sales',
    #'popup',



# You installed your paypal module to
# https://www.pythonanywhere.com/user/timetable/files/home/timetable/.virtualenvs/django17/lib/python2.7/site-packages/paypal/standard/ipn
# You might have to move it to:
# to the django folder at
# https://www.pythonanywhere.com/user/timetable/files/usr/local/lib/python2.7/dist-packages/django
# Or here is where I put it and it works:
# https://www.pythonanywhere.com/user/timetable/files/home/timetable/myDream/paypal

    #'paypal.standard.ipn',


    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SITE_ID = 1

ROOT_URLCONF = 'superDream.urls'

# Set this to true when your ssl certificate is validated.
SECURE_SSL_REDIRECT = True

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',

    # The module for Argon was not found, I think I need python3 for it.
    # It did install though.  It could be in your virtual environment
    # /home/timetable/.virtualenvs/ and you might have to move it
    # to the django folder at
# https://www.pythonanywhere.com/user/timetable/files/usr/local/lib/python2.7/dist-packages/django/contrib
    #'django.contrib.auth.hashers.Argon2PasswordHasher'
    ]


# I had to go here to get gmail to accept me sending emails from pa:
# https://accounts.google.com/DisplayUnlockCaptcha
# I also had to set my google account to accept less secure apps:
# https://www.google.com/settings/security/lesssecureapps


#EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "mail.privateemail.com"
EMAIL_HOST_USER = "dave@thehyperdream.com"
EMAIL_PORT = 465
#EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_HOST_PASSWORD = 'nvdafdx768'     # capital Kk


# Protocalls from my email provider:
# https://www.namecheap.com/support/knowledgebase/article.aspx/1179/2175/general-configuration-for-mail-clients-and-mobile-devices
# The correct host is: mail.privateemail.com

# Help online with django email:
# https://www.webforefront.com/django/setupdjangoemail.html

# Tried these TLS with EMAIL_USE_TLS = True, ports so far:
# 143, 25, 26, 110,   None of these worked.

# Tried these ssl with EMAIL_USE_SSL =True:
# 465 Worked for me sending out but not the contact form.
# 993, 995,  These two don't work.


# From namecheap:
# You need to do this:
# Outgoing server authentication should be switched on,
# SPA (secure password authentication) must be disabled.

"""
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "dpotschka11@gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#EMAIL_USE_SSL = True
EMAIL_HOST_PASSWORD = 'kipxop511'   # small k
"""

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
# We added this from the tutorial 7, customize the admin page
# this references our /mysite/templates/admin/base_site.html
# I deleted index.html it was fucking shit up.  I changed the name so
# it doesn't get accessed anymore, it must be depricated or something.
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'superDream.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# Seems to work without this next line, the images so far.
# probably because it is defined on the pa web front page.
# Which I defined.
STATIC_ROOT = '/home/timetable/superDream/myDream/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/timetable/superDream/myDream/media'

"""
This works for most browsers but not so much for chrome,
it doesn't matter, who cares how long the user can stay logged in.
To clear the sessions db I tried:
python manage.py clearsessions
It did not work because chrome remembers them for a spell.
It worked for firefox.  I think it just clears the pythonanywhere session db.
"""
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
