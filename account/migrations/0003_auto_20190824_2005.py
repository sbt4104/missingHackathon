# Generated by Django 2.1.7 on 2019-08-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190824_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='unq',
            field=models.IntegerField(default=123),
        ),
    ]
