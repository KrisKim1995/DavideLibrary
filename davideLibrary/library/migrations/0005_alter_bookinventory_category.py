# Generated by Django 5.0.6 on 2024-07-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_category_alter_bookinventory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinventory',
            name='category',
            field=models.CharField(choices=[('General Works', 'General Works'), ('Philosophy and Psychology', 'Philosophy and Psychology'), ('Religion', 'Religion'), ('Languages', 'Languages'), ('Natural Science', 'Natural Science')], default='General Works', max_length=100),
        ),
    ]
