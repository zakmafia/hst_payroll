# Generated by Django 5.0 on 2023-12-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hst_payroll_manager', '0017_alter_employee_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('pending', 'Pending'), ('inactive', 'Inactive')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('pending', 'Pending'), ('inactive', 'Inactive')], max_length=200, null=True),
        ),
    ]