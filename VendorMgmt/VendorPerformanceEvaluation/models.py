from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=200)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating = models.FloatField()
    response_time = models.FloatField()
    fulfilment_rate = models.FloatField()