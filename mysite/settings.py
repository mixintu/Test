# coding=utf-8
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))  # 把apps的文件放在里面

SECRET_KEY = '1fm-oe^1iu!^b%ahp*u^x5xj^171!^etb6!)8=)%v7oi3i=$s$'

DEBUG = True

ALLOWED_HOSTS = []

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'accounts.apps.AccountsConfig',
    'widget_tweaks',  # 自定义的表=表单组件
    'django_nose'  # 测试框架nose
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS'    : [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS' : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {
    'default': {
        # 'ENGINE'  : 'django.db.backends.sqlite3',
        # 'NAME'    : os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE'  : 'django.db.backends.mysql',
        'HOST'    : 'localhost',
        'PORT'    : '3316',
        'USER'    : 'root',
        'PASSWORD': '',
        'NAME'    : 'blog',
        # 避免映射数据库时出现警告
        'OPTIONS' : {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset'     : 'utf8mb4',
        },
    }
}

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

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
# 静态文件路径
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
# 媒体文件地址
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# 网站关键词，用于SEO
SITE_KEYWORDS = "迷心兔"

LOGIN_URL = 'login'  # 没登陆用户时的重定向名
LOGIN_REDIRECT_URL = 'post_list'  # 登陆失败后的重定向名
LOGOUT_REDIRECT_URL = 'post_list'  # 退出登录后的重定向名
