# Generated by Django 3.1.5 on 2021-01-30 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_order_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to=''),
        ),
    ]
