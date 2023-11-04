# Generated by Django 4.2.6 on 2023-11-04 12:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_remove_workingtable_product_workingtable_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.employee'),
        ),
        migrations.AddField(
            model_name='table',
            name='product',
            field=models.ManyToManyField(to='restaurant.product'),
        ),
        migrations.AddField(
            model_name='table',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_name',
            field=models.CharField(choices=[('table_1', 'Table 1'), ('table_2', 'Table 2'), ('table_3', 'Table 3')], max_length=50, verbose_name='Name'),
        ),
        migrations.DeleteModel(
            name='WorkingTable',
        ),
    ]
