from django.contrib import admin
from customer import models
# Register your models here.

admin.site.register(models.user_profile)

# admin.site.register(models.gbvariables)

class GbvariableAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

admin.site.register(models.gbvariables, GbvariableAdmin)