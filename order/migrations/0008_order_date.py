# Generated by Django 3.1.7 on 2021-04-13 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20210414_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
