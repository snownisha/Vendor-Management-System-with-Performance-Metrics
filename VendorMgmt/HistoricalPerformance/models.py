from django.db import models
from Vendor.models import Vendor

# Create your models here.
class HistoricalPerformance:
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE )
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()