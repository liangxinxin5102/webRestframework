SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # 引擎（默认）
SESSION_COOKIE_NAME="sessionid"  # Session的Cookie保存在浏览器上时的key
SESSION_COOKIE_PATH="/"              # Session的Cookie保存的路径（默认）
SESSION_COOKIE_DOMAIN = None             # Session的Cookie保存的域名（默认）
SESSION_COOKIE_SECURE = False          # 是否Https传输Cookie（默认）
SESSION_COOKIE_HTTPONLY = True        # 是否Session的Cookie只支持http传输（默认）
SESSION_COOKIE_AGE = 1209600             # Session的Cookie失效日期（2周）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期（默认）
SESSION_SAVE_EVERY_REQUEST = False # 是否每次请求都保存Session默认修改之后才保存
