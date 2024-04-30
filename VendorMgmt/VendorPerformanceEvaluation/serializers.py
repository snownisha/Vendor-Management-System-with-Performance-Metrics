from rest_framework import serializers
from .models import Vendor

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'