# Generated by Django 3.1.7 on 2021-04-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_is_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='latitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='longitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]