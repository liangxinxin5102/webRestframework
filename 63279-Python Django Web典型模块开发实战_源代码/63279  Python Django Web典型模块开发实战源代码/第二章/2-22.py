class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
class GenericViewSet(ViewSetMixin, generics.GenericAPIView):
class GenericAPIView(views.APIView):
