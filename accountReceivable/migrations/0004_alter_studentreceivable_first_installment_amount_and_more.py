# Generated by Django 4.0.4 on 2022-06-07 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountReceivable', '0003_japanschoolreceivable_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreceivable',
            name='first_installment_amount',
            field=models.IntegerField(default=0, verbose_name='First Installment'),
        ),
        migrations.AlterField(
            model_name='studentreceivable',
            name='first_installment_is_receieved',
            field=models.BooleanField(default=False, verbose_name='1st Installment Paid'),
        ),
        migrations.AlterField(
            model_name='studentreceivable',
            name='method_of_receive',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Cheque', 'Cheque'), ('Bank', 'Bank_Transfer')], default='NULL', max_length=20, verbose_name='Received Through'),
        ),
        migrations.AlterField(
            model_name='studentreceivable',
            name='remaining_installment_amount',
            field=models.IntegerField(default=0, verbose_name='Remaining Amount'),
        ),
        migrations.AlterField(
            model_name='studentreceivable',
            name='second_installment_amount',
            field=models.IntegerField(default=0, verbose_name='Second Installment'),
        ),
        migrations.AlterField(
            model_name='studentreceivable',
            name='second_installment_is_receieved',
            field=models.BooleanField(default=False, verbose_name='2nd Installment Paid'),
        ),
        migrations.AlterField(
            model_name='studentreceivable',
            name='third_installment_amount',
            field=models.IntegerField(default=0, verbose_name='Third Installment'),
        ),
        migrations.AlterField(
            model_name='studentreceivable',
            name='third_installment_is_receieved',
            field=models.BooleanField(default=False, verbose_name='3rd Installment Paid'),
        ),
    ]