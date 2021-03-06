# Generated by Django 2.1.2 on 2018-10-21 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DebitNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], db_index=True, max_length=20)),
                ('reference', models.CharField(max_length=100)),
                ('comments', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debit_notes', to='register.Company')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit_notes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DebitNoteItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('unity_of_measure', models.CharField(max_length=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, editable=False, max_digits=8)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('debit_note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit_note_items', to='transactions.DebitNote')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='register.Category')),
                ('company', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='register.Company')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='register.Machine')),
                ('pictures', models.ManyToManyField(blank=True, related_name='events', to='files.Picture')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='register.Category')),
                ('files', models.ManyToManyField(blank=True, related_name='requests', to='files.DataFile')),
                ('machine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='register.Machine')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(choices=[('low', 'Low'), ('normal', 'Normal'), ('high', 'High')], db_index=True, max_length=20)),
                ('subject', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_orders', to='register.Category')),
                ('company', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_orders', to='register.Company')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_orders', to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_orders', to='transactions.Event')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_orders', to='register.Machine')),
                ('pictures', models.ManyToManyField(blank=True, related_name='service_orders', to='files.Picture')),
            ],
        ),
        migrations.AddField(
            model_name='debitnote',
            name='service_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit_notes', to='transactions.ServiceOrder'),
        ),
    ]
