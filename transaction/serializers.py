from rest_framework import fields, serializers
from transaction import models as tnxmodels

class transactionserializer(serializers.ModelSerializer):
    class Meta:
        model = tnxmodels.transaction_model
        fields = "__all__"

