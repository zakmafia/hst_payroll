# Generated by Django 5.0 on 2023-12-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hst_payroll_manager', '0027_remove_salary_tax_salary_pension_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='net_salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]