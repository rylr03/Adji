# Generated by Django 4.2.7 on 2024-01-23 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rlclothing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]