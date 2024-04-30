from time import timezone
from django.db import models
from Vendor.models import Vendor
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Avg

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
    quality_rating = models.FloatField(null=True, blank=True)
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

def save(self, *args, **kwargs):
    super(purchaseOrder, self).save(*args, **kwargs)
    self.update_vendor_quality_rating()

def save(self, *args, **kwargs):
    super(purchaseOrder, self).save(*args, **kwargs)
    self.update_vendor_average_response_time()

def update_vendor_quality_rating(self):
    completed_orders = purchaseOrder.objects.filter(vendor=self.vendor, quality_rating__isnull=False)
    avg_quality_rating = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg']
    self.vendor.quality_rating_avg = avg_quality_rating or 0
    self.vendor.save()

def update_vendor_average_response_time(self):
    all_orders = purchaseOrder.objects.filter(vendor=self.vendor, acknowledgment_date__isnull=False)
    response_times = all_orders.annotate(
    response_time=models.F('acknowledgment_date') - models.F('issue_date')
    ).aggregate(models.Avg('response_time'))['response_time__avg']
    self.vendor.average_response_time = response_times.total_seconds() / 60 if response_times else 0
    self.vendor.save()