from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import model_meta
from supervisor.models import supervisor

class supervisorserializer(serializers.ModelSerializer):
    class Meta:
        model = supervisor
        fields = ["service_provider","balance_amount","bank_acc_no","bank_name","bank_acc_name","bank_ifsc","supervisor_is_active"]
        # fields = "__all__"

# class supervisorserialzer(serializers.Serializer):
#     service_provider = serializers.CharField()
#     supervisor_is_active = serializers.BooleanField()

class supervisorserialzerupdate(serializers.ModelSerializer):
    class Meta:
        model = supervisor
        fields = ["service_provider","bank_acc_no","bank_name","bank_acc_name","bank_ifsc"]