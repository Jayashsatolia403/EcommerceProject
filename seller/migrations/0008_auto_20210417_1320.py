# Generated by Django 3.1.7 on 2021-04-17 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_auto_20210408_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='latitude',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='longitude',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
