# Generated by Django 5.0.1 on 2024-01-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0004_remove_shipments_customer_shipments_customer_branch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipments',
            name='destination',
            field=models.CharField(choices=[('Jeddah', 'Jeddah'), ('Riyad', 'Riyad'), ('Dammam', 'Dammam')], max_length=20),
        ),
        migrations.AlterField(
            model_name='shipments',
            name='status',
            field=models.CharField(choices=[('Recieved', 'Recieved'), ('Processed', 'Processed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Feedback', 'Feedback'), ('Late', 'Late'), ('Completed', 'Completed')], default='Recieved', max_length=20),
        ),
    ]
