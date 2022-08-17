# Generated by Django 3.1.6 on 2021-08-09 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddDeviceTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mac', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CreateUserTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mac', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]