#бнбн
from app01.views import AuthView,CommonVideoView
urlpatterns = [
    #бнбн
    path('common/',CommonVideoView.as_view(),name='common'),
]
