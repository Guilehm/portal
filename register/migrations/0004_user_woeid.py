# Generated by Django 2.1.2 on 2018-10-24 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20181022_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='woeid',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
