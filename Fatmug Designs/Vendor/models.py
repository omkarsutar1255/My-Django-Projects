from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models import Avg

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
    response_time = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate a unique purchase order number using date and a sequential number
        if not self.po_number:
            today = timezone.now().date()
            last_po = PurchaseOrder.objects.filter(order_date=today).order_by('-order_date').first()

            if last_po:
                last_number = int(last_po.po_number.split('-')[-1])
                new_number = last_number + 1
            else:
                new_number = 1
            self.po_number = f'{self.vendor.vendor_code}-{today.strftime("%Y%m%d")}-{new_number:04d}'
        print("response time = ", self.response_time)
        if self.issue_date and self.acknowledgment_date:
            format_string = "%Y-%m-%d %H:%M:%S"
            print(self.issue_date, self.acknowledgment_date)
            acknowledgement_date= datetime.strptime(str(self.acknowledgment_date)[:19], format_string)
            issue_date = datetime.strptime(str(self.issue_date)[:19], format_string)
            # print(datetime.strftime(self.acknowledgment_date, '%Y-%m-%d'), datetime.strftime(self.issue_date, '%Y-%m-%d'))
            # response_time = datetime.strptime(str(acknowledgement_date - issue_date), "%Y-%m-%d %H:%M:%S")
            response_time = (acknowledgement_date - issue_date).total_seconds()
            print(response_time)
            self.response_time = response_time / 3600
            print(self.response_time)
        super().save(*args, **kwargs)
    
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
