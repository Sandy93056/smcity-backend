from django.db import models
from agent.models import agent
# Create your models here.

class CreateUserTracker(models.Model):
    user_mac = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class AddDeviceTracker(models.Model):
    user_mac = models.CharField(max_length=100)
    agent = models.ForeignKey(agent, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)

    