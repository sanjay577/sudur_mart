# Generated by Django 4.0.1 on 2022-01-18 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_orders_adress_orders_phone_orders_state_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='state',
            new_name='area',
        ),
    ]
