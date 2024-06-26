# Generated by Django 4.2.6 on 2024-02-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0010_rename_shipments_shipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='premium',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Premium'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='days_stayed',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Days Stayed '),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='deducted',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Deducted'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='stay_cost',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Stay Cost'),
        ),
    ]
