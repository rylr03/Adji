# Generated by Django 4.2.7 on 2024-01-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rlclothing', '0007_alter_customer_password1_alter_customer_password2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password2',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
