# Generated by Django 4.0.4 on 2022-10-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MA', '0044_alter_order_ref_code_alter_product_pricelbp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Ref_code',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
