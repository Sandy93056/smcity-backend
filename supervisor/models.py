# from organization.models import organization
from django.db.models.deletion import CASCADE
from customer.models import user_profile
from django.db import models
from django.contrib.auth.models import User
# # Create your models here.

class supervisor(models.Model):
    # supervisor = models.OneToOneField(User,on_delete=CASCADE, primary_key=True)
    supervisor_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_provider = models.CharField(max_length=30, null=True)
    balance_amount = models.FloatField(default=0)
    bank_acc_no = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=30)
    bank_acc_name = models.CharField(max_length=50)
    bank_ifsc = models.CharField(max_length=20)
    supervisor_is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class sup_agent(models.Model):
    sup_agent_id = models.ForeignKey(User,on_delete=models.CASCADE)
    supervisor_id = models.ForeignKey(supervisor, on_delete=models.CASCADE)



