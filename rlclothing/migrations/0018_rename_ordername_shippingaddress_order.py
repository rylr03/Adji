# Generated by Django 4.2.7 on 2024-01-27 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rlclothing', '0017_rename_order_name_shippingaddress_ordername'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='ordername',
            new_name='order',
        ),
    ]