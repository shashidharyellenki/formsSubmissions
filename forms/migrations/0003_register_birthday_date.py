# Generated by Django 4.0.4 on 2022-05-04 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_alter_register_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Birthday_date',
            field=models.DateField(default=datetime.datetime(2022, 5, 4, 10, 21, 48, 173657)),
        ),
    ]