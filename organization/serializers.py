from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import organization

class organizationserializer(serializers.ModelSerializer):
    class Meta:
        model = organization
        fields = ["balance_money", "bank_acc_no", "bank_name", "bank_acc_name", "bank_ifsc", "org_is_active"]
        # fields = "__all__"

# class organizationserialzer(serializers.Serializer):
#     service_provider = serializers.CharField()
#     org_is_active = serializers.BooleanField()

class organizationserialzerupdate(serializers.ModelSerializer):
    class Meta:
        model = organization
        fields = ["bank_acc_no","bank_name","bank_acc_name","bank_ifsc"]