from rest_framework import serializers
from .models import TuWen
class TuWenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuWen
        fields="__all__"
