from rest_framework import serializers
from .models import TeerResult

class TeerResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeerResult
        fields = '__all__'