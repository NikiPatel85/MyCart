# Generated by Django 3.0.8 on 2021-03-09 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_customer_confirmpass'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='confirmpass',
            field=models.CharField(default='', max_length=30),
        ),
    ]