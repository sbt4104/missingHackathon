# Generated by Django 2.2.1 on 2019-12-13 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190824_2005'),
        ('case', '0008_auto_20190825_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.TextField()),
                ('report_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.case')),
                ('report_task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='case.Task')),
                ('report_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile')),
            ],
        ),
    ]
