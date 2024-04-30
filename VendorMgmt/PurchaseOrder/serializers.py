from rest_framework import serializers
from .models import purchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = purchaseOrder
        fields = '__all__'