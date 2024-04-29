from rest_framework import serializers
from .models import HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'