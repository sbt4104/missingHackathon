# Generated by Django 2.1.7 on 2019-08-24 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_auto_20190824_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file1', models.FileField(blank=True, upload_to='')),
                ('file2', models.FileField(blank=True, upload_to='')),
                ('file3', models.FileField(blank=True, upload_to='')),
                ('csvfile1', models.FileField(blank=True, upload_to='')),
                ('csvfile2', models.FileField(blank=True, upload_to='')),
                ('url1', models.URLField(blank=True)),
                ('url2', models.URLField(blank=True)),
            ],
        ),
    ]
