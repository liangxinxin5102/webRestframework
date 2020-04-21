REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', #必须有
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}
import datetime
JWT_AUTH = {
 # 指明token的有效期
 'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}
