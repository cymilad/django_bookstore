# Generated by Django 5.1.3 on 2024-11-26 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
