from django.urls import path
from .views import PurchaseOrderListCreate, PurchaseOrderRetrieveUpdateDestroy

urlpatterns = [
    path('api/purchase_orders/', PurchaseOrderListCreate.as_view(), name='purchase_order_list_create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroy.as_view(), name='purchase_order_retrieve_update_destroy'),
]