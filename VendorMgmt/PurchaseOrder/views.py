from time import timezone
from django.shortcuts import render
from .models import purchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = purchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = purchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class AcknowledgePurchaseOrder(APIView):
    def post(self, request, po_id):
        try:
            purchase_order = purchaseOrder.objects.get(pk=po_id)
        except purchaseOrder.DoesNotExist:
            return Response({"error": "Purchase Order not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Update acknowledgment date
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()
        
        # Trigger recalculation of average_response_time
        purchase_order.vendor.calculate_average_response_time()
        
        return Response({"message": "Purchase Order acknowledged successfully"}, status=status.HTTP_200_OK)