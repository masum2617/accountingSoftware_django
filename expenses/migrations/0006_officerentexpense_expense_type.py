# Generated by Django 4.0.4 on 2022-05-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_dailyexpense_is_paid_documentrenewalexpense_is_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='officerentexpense',
            name='expense_type',
            field=models.CharField(default='Office Rent', max_length=50),
        ),
    ]
