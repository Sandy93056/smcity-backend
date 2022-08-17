# Generated by Django 3.1.6 on 2021-08-22 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_auto_20210728_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='smarttoilet',
            fields=[
                ('smt_id', models.AutoField(primary_key=True, serialize=False)),
                ('waterlevel', models.FloatField()),
                ('is_available', models.BooleanField()),
                ('descripton', models.TextField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
            ],
        ),
    ]
