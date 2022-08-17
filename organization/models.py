from django.db import models

# # Create your models here.

class organization(models.Model):
    organization_id = models.AutoField(primary_key=True)
    balance_money = models.FloatField()
    bank_acc_no = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    bank_acc_name = models.CharField(max_length=50)
    bank_ifsc = models.CharField(max_length=30)
    org_is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class organization_agent_list(models.Model):
    organisation = models.ForeignKey(organization, on_delete=(models.CASCADE))
    org_agent_phone = models.IntegerField()


