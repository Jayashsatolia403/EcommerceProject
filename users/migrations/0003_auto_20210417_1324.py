# Generated by Django 3.1.7 on 2021-04-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_is_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='latitude',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='longitude',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
