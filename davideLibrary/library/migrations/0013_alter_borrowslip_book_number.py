# Generated by Django 5.0.6 on 2024-08-05 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_remove_bookinventory_barcode_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowslip',
            name='book_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
