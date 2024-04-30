from time import timezone
from django.db import models
from Vendor.models import Vendor
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class purchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status_choices = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ]
    status = models.CharField(max_length=50, choices=status_choices)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

@receiver(post_save, sender=purchaseOrder)
def calculate_on_time_delivery_rate(sender, instance, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        completed_orders = purchaseOrder.objects.filter(vendor=vendor, status='completed')
        total_completed_orders = completed_orders.count()
        delivered_on_time = completed_orders.filter(delivery_date__lte=timezone.now()).count()
        if total_completed_orders > 0:
            on_time_delivery_rate = (delivered_on_time / total_completed_orders) * 100
            vendor.on_time_delivery_rate = on_time_delivery_rate
            vendor.save()