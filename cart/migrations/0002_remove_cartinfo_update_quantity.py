# Generated by Django 3.1.7 on 2021-04-20 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartinfo',
            name='update_quantity',
        ),
    ]
