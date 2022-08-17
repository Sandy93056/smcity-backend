from django.db import models
from django.contrib.auth.models import User
from device.models import device
# Create your models here.

class transaction_model(models.Model):
    txn_id = models.CharField(max_length=100, primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    device = models.ForeignKey(device, on_delete=models.CASCADE, null=False)
    txn_amt = models.FloatField(null=False)
    txn_status = models.CharField(max_length=50, default="none")
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=150, default="No Description Available")
    transaction_type = models.CharField(max_length=150, null=False, default="online")

class addmoney_model(models.Model):
    addmoney_id = models.CharField(max_length=100, primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_amount = models.FloatField()
    order_currency = models.CharField(max_length=20,null=False)
    adm_status = models.CharField(max_length=50,default="none")