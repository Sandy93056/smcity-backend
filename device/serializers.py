from django.db import models
from django.db.models import fields
from rest_framework import serializers 
from device.models import device, dustbin, smarttoilet, washroom, waterpoint

class deviceserializer(serializers.ModelSerializer):
    class Meta:
        model = device
        # fields = "__all__"
        fields = ["device_id","device_lat", "device_long", "is_active","device_mac", "device_type","privlaged_user"]
        


class dustbinserializer(serializers.ModelSerializer):
    class Meta:
        model = dustbin
        fields = "__all__"
        # fields = []

class waterpointserializer(serializers.ModelSerializer):
    class Meta:
        model = waterpoint
        fields = "__all__"
        # fields = ["water_level"]
class washroomserializer(serializers.ModelSerializer):
    class Meta:
        model = washroom
        fields = "__all__"


class deviceserializer(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = "__all__"
        # fields = ["device_id","device_lat", "device_long", "is_active","device_mac", "device_type","privlaged_user"]
        

# Update API's

class updatedeviceserializer(serializers.ModelSerializer):
    class Meta:
        model = device
        # fields = "__all__"
        fields = ["device_lat", "device_long", "is_active","device_type","privlaged_user"]
 

class updatedustbinserializer(serializers.ModelSerializer):
    class Meta:
        model = dustbin
        # fields = "__all__"
        fields = ["bin_total_volume","bin_total_height"," bin_avai_volume"]

class updatewaterpointserializer(serializers.ModelSerializer):
    class Meta:
        model = waterpoint
        # fields = "__all__"
        fields = ["total_water_capacity","water_available"]
class updatewashroomserializer(serializers.ModelSerializer):
    class Meta:
        model = washroom
        fields = "__all__"

class smarttoiletserializer(serializers.ModelSerializer):
    class Meta:
        model = smarttoilet
        fields = "__all__"