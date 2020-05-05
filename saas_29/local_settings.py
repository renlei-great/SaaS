
#--------- SMS　发送短信 ------------------
SMS_APPID = 1400363965
SMS_APPKEY = "29db342d893fdd207ac680cc7446b7c7"
SMS_TEMPLATE = {
    'login': 596948,
    'register': 596993,
}


ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'saas_test',
        'USER': 'root',
        'PASSWORD': 'ubuntu',
        'HOST': 'localhost',
        'PORT': 3306
    }
}