# Generated by Django 3.2.3 on 2021-07-26 15:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0012_auto_20210210_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='timer_active',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='timer_pause',
        ),
    ]
