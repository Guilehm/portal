# Generated by Django 2.1.2 on 2018-10-20 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_auto_20181020_1527'),
        ('register', '0002_datafile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DataFile',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
