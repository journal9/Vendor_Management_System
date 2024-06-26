# Generated by Django 5.0.4 on 2024-05-06 07:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0002_alter_po_vendor'),
        ('vendor', '0002_vendorsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='POModel',
            fields=[
                ('po_id', models.AutoField(primary_key=True, serialize=False)),
                ('po_number', models.CharField(max_length=20, unique=True)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('delivery_date', models.DateTimeField()),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.TextField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending')),
                ('quality_rating', models.FloatField(null=True)),
                ('issue_date', models.DateTimeField(editable=False)),
                ('acknowledgment_date', models.DateTimeField(editable=False, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendorsmodel')),
            ],
            options={
                'ordering': ['-order_date'],
            },
        ),
    ]
