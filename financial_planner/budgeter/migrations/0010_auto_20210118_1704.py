# Generated by Django 3.1.4 on 2021-01-18 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeter', '0009_auto_20210118_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_posted',
            field=models.DateField(default='0101"/"1818"/"21'),
        ),
    ]
