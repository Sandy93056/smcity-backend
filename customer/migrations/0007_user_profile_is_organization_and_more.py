# Generated by Django 4.1 on 2022-08-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_gbvariables'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='is_organization',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='is_supervisor',
            field=models.BooleanField(default=False),
        ),
    ]
