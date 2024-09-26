# Generated by Django 4.2.15 on 2024-09-26 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0031_merge_20240908_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=50, verbose_name='Status English')),
                ('name_ar', models.CharField(max_length=50, verbose_name='Status Arabic')),
            ],
            options={
                'verbose_name': 'Shipment Status',
                'verbose_name_plural': 'Shipment Statuses',
            },
        ),
        migrations.AlterField(
            model_name='shipment',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shipments.shipmentstatus', verbose_name='Status'),
        ),
    ]