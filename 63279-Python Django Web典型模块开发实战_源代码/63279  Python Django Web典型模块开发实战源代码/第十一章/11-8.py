CACHES = {
 'default': {
  'BACKEND': 'django.core.cache.backends.dummy.DummyCache',  # 缓存后台使用的引擎
  'TIMEOUT': 300,            # 缓存超时时间（默认300秒，None表示永不过期，0表示立即过期）
  'OPTIONS':{
   'MAX_ENTRIES': 300,          # 最大缓存记录的数量（默认300）
   'CULL_FREQUENCY': 3,          # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
  },
 }
}
