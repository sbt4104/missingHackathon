# Generated by Django 2.2.1 on 2019-12-13 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190824_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='unq',
        ),
    ]
