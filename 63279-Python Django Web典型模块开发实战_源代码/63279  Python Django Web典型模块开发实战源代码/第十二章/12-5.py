DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '12a',
        'USER':'root',
        'PASSWORD':'mysql密码',
        'HOST':'127.0.0.1',
        "OPTIONS":{"init_command":"SET default_storage_engine=INNODB;"}#第三方登录功能必须加上
    }
}
