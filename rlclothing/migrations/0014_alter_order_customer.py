# Generated by Django 4.2.7 on 2024-01-27 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rlclothing', '0013_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='rlclothing.customer'),
        ),
    ]
