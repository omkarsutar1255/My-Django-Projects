from django.db import models
from datetime import datetime
from django.utils import timezone
# from django.db.models import Avg
from django.contrib.auth.models import User

class BaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True

class Vendor(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    contact_details = models.PositiveIntegerField(unique=True)
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    quality_rating_avg = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    average_response_time = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fulfillment_rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    
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

class PurchaseOrder(BaseModel):
    po_number = models.CharField(max_length=50, primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20,choices=order_status,null=True,blank=True, validators=[validate_status], default="Pending")
    quality_rating = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True,blank=True)
    response_time = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    on_time_delivery = models.BooleanField(default=False)
    # on_time_delivery_rate = models.FloatField(null=True,blank=True)

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
        format_string = "%Y-%m-%d %H:%M:%S"
        if self.issue_date and self.acknowledgment_date:
            print(self.issue_date, self.acknowledgment_date)
            acknowledgement_date= datetime.strptime(str(self.acknowledgment_date)[:19], format_string)
            issue_date = datetime.strptime(str(self.issue_date)[:19], format_string)
            # print(datetime.strftime(self.acknowledgment_date, '%Y-%m-%d'), datetime.strftime(self.issue_date, '%Y-%m-%d'))
            # response_time = datetime.strptime(str(acknowledgement_date - issue_date), "%Y-%m-%d %H:%M:%S")
            response_time = (acknowledgement_date - issue_date).total_seconds()
            print(response_time)
            self.response_time = response_time / 3600
            print(self.response_time)
        if self.status == "Completed":
            if self.delivery_date == None:
                print("setting True1")
                self.delivery_date = datetime.now()
                self.on_time_delivery = True
            elif datetime.strptime(str(self.delivery_date)[:19], format_string) > datetime.now():
                print("setting True False")
                self.on_time_delivery = True
        print("new")

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.po_number

class HistorialPerformance(BaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    on_time_delivery_rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    quality_rating_avg = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    average_response_time = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fulfillment_rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.vendor.name
