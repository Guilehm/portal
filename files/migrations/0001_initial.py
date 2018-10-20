# Generated by Django 2.1.2 on 2018-10-20 15:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='register/datafile/file')),
                ('original_file_name', models.CharField(blank=True, max_length=500, null=True)),
                ('extension', models.CharField(blank=True, max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='register/picture/image')),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_changed', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
