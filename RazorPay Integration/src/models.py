from django.db import models


class Coffee(models.Model):
    name = models.CharField(max_length=1000, blank=True)
    amount = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, default='')
    order_id = models.CharField(max_length=1000)
    # razorpay_payment_id = models.CharField(max_length=1000, blank=True)
    paid = models.BooleanField(default=False)
