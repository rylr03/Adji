# Generated by Django 4.2.7 on 2024-01-27 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rlclothing', '0009_remove_customer_password1_remove_customer_password2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
    ]
