# Generated by Django 4.0.4 on 2022-05-06 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_alter_register_birthday_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]