# Generated by Django 4.2.7 on 2024-01-30 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rlclothing', '0025_alter_orderapproval_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderapproval',
            old_name='order',
            new_name='order_name',
        ),
    ]
