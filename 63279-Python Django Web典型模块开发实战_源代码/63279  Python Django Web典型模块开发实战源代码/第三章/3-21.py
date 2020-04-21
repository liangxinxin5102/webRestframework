from app01.views import TypeView
urlpatterns = [
    #......
    path('api/type/',TypeView.as_view())
]
