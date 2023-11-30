from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from .models import *

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_avg_response_time(sender, instance, **kwargs):
    vendor = instance.vendor
    print("vendor = ", vendor)
    # Calculate the new average response time for the vendor
    # response_times = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False).values_list('response_time', flat=True)
    avg_response_time = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False).aggregate(avg_response_time=Avg('response_time'))

    # Update the vendor's avg_response_time field
    print("avg_response_time = ", avg_response_time['avg_response_time'])
    vendor.average_response_time = avg_response_time['avg_response_time']
    vendor.save()
    # def save(self, *args, **kwargs):
    #     average_time = PurchaseOrder.objects.filter(vendor=self.id).aggregate(avg_response_time=Avg('response_time'))
    #     print(average_time['avg_response_time'])
    #     self.average_response_time = average_time['avg_response_time']
    #     super().save(*args, **kwargs)