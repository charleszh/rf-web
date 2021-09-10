from .base import *


INSTALLED_APPS += [
        'debug_toolbar',
        ]
MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        ]
INTERNAL_IPS = ['127.0.0.1']
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
]

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_data',
        'USER': 'root',
        'PASSWORD': 'test1234',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'TEST': {
            'CHARSET': 'utf-8',
            'COLLATION': 'utf8-general-cli'
        }
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        #"BACKEND": "redis_cache.RedisCache",
        #"LOCATION": "redis://127.0.0.1:6379",
        #"OPTIONS": {
        #    "CONNECTION_POOL_CLASS": "redis.BlockingConnectionPool",
        #    "CONNECTION_POOL_CLASS_KWARGS": {"max_connections": 50, "timeout": 20},
        #    "MAX_CONNECTIONS": 1000,
        #    "PICKLE_VERSION": -1,
        #}

    }
}
