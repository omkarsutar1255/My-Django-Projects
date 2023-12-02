from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Avg
from .models import *

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_avg_response_time(sender, instance, **kwargs):
    vendor = instance.vendor
    print("vendor = ", vendor)
    print(vendor.on_time_delivery_rate,vendor.quality_rating_avg, vendor.average_response_time,vendor.fulfillment_rate)
    if vendor.on_time_delivery_rate or vendor.quality_rating_avg or vendor.average_response_time or vendor.fulfillment_rate:
        HistorialPerformance.objects.create(vendor=vendor, on_time_delivery_rate=vendor.on_time_delivery_rate,
                                        quality_rating_avg=vendor.quality_rating_avg, average_response_time=vendor.average_response_time,
                                        fulfillment_rate=vendor.fulfillment_rate)
    avg_response_time = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False).aggregate(avg_response_time=Avg('response_time'))

    print("avg_response_time = ", avg_response_time['avg_response_time'])
    vendor.average_response_time = avg_response_time['avg_response_time']

    print("inside fulfillment")
    completed = PurchaseOrder.objects.filter(vendor=vendor, status="Completed").count()
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    print(completed, total_orders)
    vendor.fulfillment_rate = completed / total_orders * 100
    quality_rating = PurchaseOrder.objects.filter(vendor=vendor).aggregate(rating_avg=Avg('quality_rating'))
    vendor.quality_rating_avg = quality_rating['rating_avg']
    if completed:
        on_time_delivery = PurchaseOrder.objects.filter(vendor=vendor, on_time_delivery=True).count()
        print(on_time_delivery, completed)
        vendor.on_time_delivery_rate = on_time_delivery / completed * 100    
    vendor.save()
