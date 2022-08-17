from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import model_meta
from agent.models import agent

class agentserializer(serializers.ModelSerializer):
    class Meta:
        model = agent
        fields = ["service_provider","balance_amount","bank_acc_no","bank_name","bank_acc_name","bank_ifsc","agent_is_active"]
        # fields = "__all__"

# class agentserialzer(serializers.Serializer):
#     service_provider = serializers.CharField()
#     agent_is_active = serializers.BooleanField()

class agentserialzerupdate(serializers.ModelSerializer):
    class Meta:
        model = agent
        fields = ["service_provider","bank_acc_no","bank_name","bank_acc_name","bank_ifsc"]