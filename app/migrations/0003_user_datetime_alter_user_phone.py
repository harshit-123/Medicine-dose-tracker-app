# Generated by Django 4.2.1 on 2023-05-04 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_user_fname_remove_user_lname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 5, 4, 10, 22, 40, 770740, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
