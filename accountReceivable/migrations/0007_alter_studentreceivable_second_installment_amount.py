# Generated by Django 4.0.4 on 2022-06-08 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountReceivable', '0006_alter_studentreceivable_first_installment_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreceivable',
            name='second_installment_amount',
            field=models.IntegerField(default=0, verbose_name='Second Installment'),
        ),
    ]