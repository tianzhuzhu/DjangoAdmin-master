# Generated by Django 2.2 on 2021-07-19 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myoperations', '0005_auto_20210719_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='operation_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 19, 15, 29, 33, 608196), verbose_name='操作时间'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='operation_type',
            field=models.CharField(choices=[('1', '增ip'), ('2', '减ip')], max_length=32, verbose_name='操作原因'),
        ),
    ]
