from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vendor

# Create your views here.
class VendorPerformanceView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            performance_metrics = {
                'on_time_delivery_rate': vendor.on_time_delivery_rate,
                'quality_rating': vendor.quality_rating,
                'response_time': vendor.response_time,
                'fulfilment_rate': vendor.fulfilment_rate,
            }
            return Response(performance_metrics)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=404)