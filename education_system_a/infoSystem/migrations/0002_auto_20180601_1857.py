# Generated by Django 2.0.5 on 2018-06-01 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('User_ID', models.CharField(default=None, max_length=20, primary_key=True, serialize=False)),
                ('Error_time', models.IntegerField()),
                ('Lock_out', models.DateTimeField(default=datetime.datetime(2018, 6, 1, 18, 57, 46, 647511))),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to='temp/cover-img/'),
        ),
    ]
