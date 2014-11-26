# -*- coding: UTF-8 -*-
# Django settings for chongwug project.
import os
from django.conf.urls import url
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(os.path.split(os.path.dirname(__file__))[0], 'static').replace('\\','/')

if 'SERVER_SOFTWARE' in os.environ:
    DEBUG = False
    TEMPLATE_DEBUG = False
    
    ADMINS = [
              '692673390@qq.com',
             ]
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = False
    EMAIL_HOST = 'smtp.163.com'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = 'fccsl6321@163.com'
    EMAIL_HOST_PASSWORD = '8792833'
    
    MYSQL_HOST = 'rdsaera2yaera2y.mysql.rds.aliyuncs.com'
    MYSQL_PORT = '3306'
    MYSQL_USER = 'chongwug'
    MYSQL_PASS = 'weet6321'
    MYSQL_DB   = 'chongwug'
    
    # Hosts/domain names that are valid for this site; required if DEBUG is False
    # See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ['.chongwug.com','.chongwug.com.']
    WAP_ROOT = 'http://m.chongwug.com'
    
    STATIC_PATH_URL = url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT,'show_indexes':False  })
    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = 'http://www.chongwug.com/static/'
    CKEDITOR_STATIC_URL = '//chongwug-cdn.b0.upaiyun.com/lib/'
elif 'TEST_SERVER' in os.environ:
    DEBUG = False
    TEMPLATE_DEBUG = False
    
    ADMINS = [
              '692673390@qq.com',
             ]
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = False
    EMAIL_HOST = 'smtp.163.com'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = 'fccsl6321@163.com'
    EMAIL_HOST_PASSWORD = '8792833'
    
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'
    MYSQL_USER = 'root'
    MYSQL_PASS = ''
    MYSQL_DB   = 'chongwug'
    
    # Hosts/domain names that are valid for this site; required if DEBUG is False
    # See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ['.cwg.com','.cwg.com.','192.168.1.100','192.168.1.100.']
    WAP_ROOT = '192.168.1.100/m/'
    STATIC_PATH_URL = url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT,'show_indexes':False  })
    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = 'http://www.chongwug.com/static/'
    CKEDITOR_STATIC_URL = '//chongwug-cdn.b0.upaiyun.com/lib/'
else:
    DEBUG = True
    TEMPLATE_DEBUG = True
    
    ADMINS = [
              '692673390@qq.com',
             ]
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = False
    EMAIL_HOST = 'smtp.163.com'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = 'fccsl6321@163.com'
    EMAIL_HOST_PASSWORD = '8792833'
    
   # Make `python manage.py syncdb` works happy!
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'
    MYSQL_USER = 'root'
    MYSQL_PASS = ''
    MYSQL_DB   = 'chongwug'
    
    # Hosts/domain names that are valid for this site; required if DEBUG is False
    # See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ['localhost']
    WAP_ROOT = '/m'
    STATIC_PATH_URL = url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT,'show_indexes':False  })
    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = 'http://localhost:8000/static/'
    CKEDITOR_STATIC_URL = 'http://localhost:8000/static/lib/dist/'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': MYSQL_DB,                      # Or path to database file if using sqlite3.
        'USER': MYSQL_USER,                      # Not used with sqlite3.
        'PASSWORD': MYSQL_PASS,                  # Not used with sqlite3.
        'HOST': MYSQL_HOST,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': MYSQL_PORT,                      # Set to empty string for default. Not used with sqlite3.
    }
}

#for local test min static files, set this value to True
PROD_TEST = False
CDN_TEST = False



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = STATIC_ROOT + 'manage/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://www.chongwug.com/static/manage/'

WEB_CONFIG_ROOT = os.path.join(os.path.split(os.path.dirname(__file__))[0], 'static').replace('\\','/')

ROOT = os.path.split(os.path.dirname(__file__))[0].replace('\\','/')
PIC_ROOT = "http://chongwug-pic.b0.upaiyun.com"
PET_FARM_PIC_ROOT = "/farmpic/"
PET_AD_PIC_ROOT = "/gfile/"
PET_PIC_ROOT = "/petpic/"
CDN_ROOT = "//chongwug-cdn.b0.upaiyun.com"
SUPPLIE_PIC_ROOT = "/suppliepic/"
PIC_TMP_PATH = "/manage/pictest/"
ALIPAY_ID = '2088611905683894'
ALIPAY_KEY = 'xjmcw6c697a2t10gji4l1mu1hqeqe84g'
ALIPAY_EMAIL = 'zhifubao@chongwug.com'
from alipay import Alipay,WapAlipay
ALIPAY = Alipay(pid=ALIPAY_ID, key=ALIPAY_KEY, seller_email=ALIPAY_EMAIL)
WAPALIPAY = WapAlipay(pid=ALIPAY_ID, key=ALIPAY_KEY, seller_email=ALIPAY_EMAIL)
SESSION_COOKIE_AGE = 60 * 30#session 30min 

# Additional locations of static files
STATICFILES_DIRS = (
                    #os.path.join(os.path.split(os.path.dirname(__file__))[0], 'static/src').replace('\\','/'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

CKEDITOR_MEDIA_PREFIX = "/static/ckeditor/" 
CKEDITOR_UPLOAD_PATH = "pictest/" 
CKEDITOR_UPLOAD_PREFIX = MEDIA_URL + "pictest/"
CKEDITOR_RESTRICT_BY_USER=False
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':[       
            ['PasteText','PasteFromWord','Undo','Redo','-','SelectAll'],
            ['Bold','Italic','NumberedList','BulletedList','-','Outdent','Indent'],        
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock','Font','FontSize'],
            ['Maximize']        
        ],
        'width': 700,
        'height': 200,
        'toolbarCanCollapse': False,
    },
}
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^p=b)e@s8ksya&amp;wo^b1+)e3)rho7fgws26)gowr5lm^q5-h!f&amp;'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'chongwug.commom.SubdomainMiddleware',
    'django.middleware.common.CommonMiddleware',
    'chongwug.mysessionmiddleware.mySessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'chongwug.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'chongwug.wsgi.application'

TEMPLATE_DIRS = (
                 os.path.join(os.path.split(os.path.dirname(__file__))[0], 'static').replace('\\','/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customer',
    'back_manager',
    'petfarm',
    'manager',
    'marketer',
    'ckeditor',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)


from django.utils.log import AdminEmailHandler
from django.core.mail  import  send_mail
from django.views.debug import get_exception_reporter_filter
import traceback
class myAdminEmailHandler(AdminEmailHandler):
    def emit(self, record):
        stack_trace = '\n'.join(traceback.format_exception(*record.exc_info))
        try:
            request = record.request
            subject = '%s ( IP): %s' % (
                record.levelname,
                record.getMessage()
            )
            filter = get_exception_reporter_filter(request)
            request_repr = filter.get_request_repr(request)
        except Exception:
            subject = '%s: %s' % (
                record.levelname,
                record.getMessage()
            )
            request = None
            request_repr = "Request repr() unavailable."
        message = "%s\n\n%s" % (stack_trace, request_repr)
        sender=EMAIL_HOST_USER
        mail_list= ADMINS
        send_mail(
                    subject=subject,  
                    message=message,  
                    from_email=sender,
                    recipient_list=mail_list,  
                    fail_silently=False,  
                    connection=None  
                )
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'chongwug.settings.myAdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}