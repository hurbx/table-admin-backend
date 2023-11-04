# Generated by Django 4.2.6 on 2023-11-04 11:51

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_remove_table_creation_date_remove_table_employee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.employee')),
                ('products', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.product')),
                ('table', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.table')),
            ],
            options={
                'verbose_name': 'WorkingTable',
                'verbose_name_plural': 'WorkingTables',
            },
            managers=[
                ('workingtable', django.db.models.manager.Manager()),
            ],
        ),
    ]