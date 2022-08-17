from django.contrib import admin
from transaction.models import transaction_model,addmoney_model
# Register your models here.

admin.site.register(addmoney_model)
admin.site.register(transaction_model)