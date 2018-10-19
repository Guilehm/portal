# Generated by Django 2.1.2 on 2018-10-19 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_worker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
