INSTALLED_APPS = [
#……
    'app01.apps.App01Config',
    'rest_framework',
    'corsheaders'
]
#......
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',#放到中间件顶部
    'django.middleware.security.SecurityMiddleware',
#……
]
#......
CORS_ORIGIN_ALLOW_ALL = True
