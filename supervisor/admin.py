from django.contrib import admin
from .models import supervisor, sup_agent

# Register your models here.

admin.site.register(supervisor)
admin.site.register(sup_agent)