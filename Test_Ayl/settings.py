"""
Django settings for Test_Ayl project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f=*3thk7&qt0ca^)%iz-pg*cvz7_67h5+l2u@s7*rwuf7gm98k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'Dcc',
    'django_crontab'
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

ROOT_URLCONF = 'Test_Ayl.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Test_Ayl.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR+'/db/', 'db.sqlite3'),
#     }
# }
# print('11111',BASE_DIR)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'test_ayl',  # 数据库名，先前创建的
        'USER': os.getenv("MYSQLUSER","root"),     # 用户名，可以自己创建用户
        'PASSWORD': os.getenv("MYSQLPASSWD","abc1234"),  # 密码
        # 'HOST': "127.0.0.1",  # mysql服务所在的主机ip
        'HOST': os.getenv("MYSQLLINK","mysql"),  # mysql服务所在的主机ip
        # 'HOST': os.getenv("MYSQLLINK","192.168.43.142"),  # mysql服务所在的主机ip

        'PORT': '3306',         # mysql服务端口
        'OPTIONS': {
                    "init_command": "SET foreign_key_checks = 0;",
                },
        'TEST': {
                    'CHARSET' : 'utf8',
                    'COLLATION':'utf8_general_ci'
                }
            }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'     # 这里修改了

TIME_ZONE = 'Asia/Shanghai'    # 这里修改了

USE_I18N = True

USE_L10N = True

USE_TZ = False    # 这里修改了


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# 邮件服务配置文件
EMAIL_USE_SSL = True
# 邮箱服务
EMAIL_HOST = 'smtp.qq.com'
# 端口号
EMAIL_PORT = 465
# 账号
EMAIL_HOST_USER = '122903166@qq.com'
# 授权秘钥 密钥要在QQ邮箱内开启IMAP/SMTP服务会获得
EMAIL_HOST_PASSWORD = 'ahovrotvonzibiei'
# 发件人
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

CRONJOBS=[('*/1 * * * *', 'Dcc.cron.test','>>test.log')]