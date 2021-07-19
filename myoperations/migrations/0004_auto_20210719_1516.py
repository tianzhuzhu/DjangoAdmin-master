# Generated by Django 2.2 on 2021-07-19 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myoperations', '0003_auto_20210719_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='opetaion_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='operation',
            name='type',
        ),
        migrations.AlterField(
            model_name='operation',
            name='operation_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 19, 15, 16, 8, 897524), verbose_name='操作时间'),
        ),
    ]
