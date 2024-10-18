from .settings import *

DATABASES = {
    "default":
        {
            "ENGINE": 'django.db.backends.mysql',
            "NAME": 'blog2db',
            "USER": 'root',
            "PASSWORD": 'root',
            "HOST": '127.0.0.1',
            "PORT": '3306',
        }
}