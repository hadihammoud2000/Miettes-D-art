# Generated by Django 3.0.1 on 2022-03-14 11:29

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('MA', '0036_auto_20220314_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, editable=False, max_length=200, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Email',
            field=models.EmailField(blank=True, editable=False, max_length=254, null=True),
        ),
    ]