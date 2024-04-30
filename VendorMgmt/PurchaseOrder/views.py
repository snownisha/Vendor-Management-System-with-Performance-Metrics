from django.shortcuts import render
from .models import purchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework import generics


# Create your views here.
class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = purchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = purchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer