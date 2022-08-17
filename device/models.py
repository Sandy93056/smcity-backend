from django.db.models.deletion import CASCADE
from agent.models import agent
from django.db import models

# Create your models here.


class device(models.Model):
    device_id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(agent, on_delete=CASCADE)
    device_lat = models.FloatField(null=False)
    device_long = models.FloatField(null=False)
    is_active = models.BooleanField(default=False)
    device_mac = models.CharField(max_length=100, unique=True)
    device_type = models.CharField(max_length=30, null=False)
    privlaged_user = models.TextField(null=True)
    
    
class dustbin(models.Model):
    dust_id = models.AutoField(primary_key=True)
    device = models.OneToOneField(device, on_delete=CASCADE)
    # dustbin_level = models.FloatField(null=False)
    bin_total_volume = models.FloatField(default="20")
    bin_total_height = models.FloatField(default="20")
    bin_avai_volume = models.FloatField(default="20")

class waterpoint(models.Model):
    wp_id =  models.AutoField(primary_key=True)
    device = models.OneToOneField(device, on_delete=models.CASCADE)
    # water_level = models.FloatField(null=False)
    total_water_capacity = models.FloatField(default="20")
    water_available = models.FloatField(default="20")

class washroom(models.Model):
    washroom_id = models.AutoField(primary_key=True)
    device_id = models.OneToOneField(device, on_delete=CASCADE)
    no_of_urinal = models.IntegerField(null=False)
    no_of_pots = models.IntegerField(null=False)
    no_of_bath = models.IntegerField(null=False)
    urinal_filled = models.IntegerField(null=True)
    pot_filled = models.IntegerField(null=True)
    bath_filled = models.IntegerField(null=True)
    
    
class smarttoilet(models.Model):
    smt_id = models.AutoField(primary_key=True)
    device = models.ForeignKey(device, on_delete=models.CASCADE)
    waterlevel = models.FloatField()
    is_available = models.BooleanField(default=True)
    description = models.TextField()

class device_type_availaable(models.Model):
    sno = models.AutoField(primary_key=True)
    device_type = models.CharField(max_length=30)

