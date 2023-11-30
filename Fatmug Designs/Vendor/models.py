from django.db import models
from datetime import datetime
import uuid

class Vendor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    contact_details = models.TextField(unique=True)
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(null=True,blank=True)
    quality_rating_avg = models.FloatField(null=True,blank=True)
    average_response_time = models.FloatField(null=True,blank=True)
    fulfillment_rate = models.FloatField(null=True,blank=True)
    
    def __str__(self):
        return self.name


order_status = (('Pending','Pending'),('Completed','Completed'),('Cancelled','Cancelled'))
def validate_status(value):
    valid_choices = [choice[0] for choice in order_status]
    print(valid_choices, value)
    if value not in valid_choices:
        return False
    else:
        return True

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20,choices=order_status,null=True,blank=True, validators=[validate_status], default="Pending")
    quality_rating = models.FloatField(null=True,blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True,blank=True)

    def save(self, *args, **kwargs):
        self.po_number = f'{self.vendor.name}-{datetime.now().year}-{uuid.uuid4()}'
        return super(PurchaseOrder,self).save(*args,**kwargs)
    def __str__(self):
        return self.po_number


class HistorialPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        self.vendor.name
