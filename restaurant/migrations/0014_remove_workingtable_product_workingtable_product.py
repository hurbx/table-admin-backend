# Generated by Django 4.2.6 on 2023-11-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_remove_workingtable_products_workingtable_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workingtable',
            name='product',
        ),
        migrations.AddField(
            model_name='workingtable',
            name='product',
            field=models.ManyToManyField(to='restaurant.product'),
        ),
    ]
