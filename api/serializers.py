from rest_framework import serializers
from .models import DataLogger

class DataLoggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataLogger
        fields = '__all__'
