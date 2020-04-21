from .models import Type
class TypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Type
        fields="__all__"
