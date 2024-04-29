# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/vendors/', views.vendor_list),
    path('api/vendors/<int:pk>/', views.vendor_detail),
]
