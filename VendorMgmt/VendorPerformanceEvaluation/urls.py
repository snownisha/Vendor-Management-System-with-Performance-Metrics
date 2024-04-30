from django.urls import path
from .views import VendorPerformanceView

urlpatterns = [
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view()),
]