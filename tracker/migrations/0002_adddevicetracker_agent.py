# Generated by Django 3.1.6 on 2021-08-10 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adddevicetracker',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agent.agent'),
        ),
    ]
