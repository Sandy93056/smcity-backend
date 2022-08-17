from django.contrib import admin
from .models import organization, organization_agent_list

# Register your models here.

admin.site.register(organization)
admin.site.register(organization_agent_list)
