# Generated by Django 5.0.4 on 2024-05-30 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='store_cutom_last_na_723f5c_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_cutomers',
        ),
    ]
