# Generated by Django 3.2.4 on 2021-06-24 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user_photo',
            field=models.ImageField(default='images/profileimage/default_profile_img.jpg', null=True, upload_to='images/profileimage/'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_type',
            field=models.CharField(default='customer', max_length=20),
        ),
    ]
