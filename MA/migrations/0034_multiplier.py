# Generated by Django 3.0.1 on 2022-03-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MA', '0033_auto_20220314_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multiplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USDtoLBP', models.IntegerField(default=14000)),
            ],
        ),
    ]
