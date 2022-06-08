# Generated by Django 4.0.4 on 2022-06-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountReceivable', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentreceivable',
            old_name='is_pending',
            new_name='first_installment_is_pending',
        ),
        migrations.RenameField(
            model_name='studentreceivable',
            old_name='is_received',
            new_name='first_installment_is_receieved',
        ),
        migrations.RenameField(
            model_name='studentreceivable',
            old_name='is_rejected',
            new_name='first_installment_is_rejected',
        ),
        migrations.RenameField(
            model_name='studentreceivable',
            old_name='receivable_amount',
            new_name='total_fees',
        ),
        migrations.AddField(
            model_name='studentreceivable',
            name='first_installment_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentreceivable',
            name='remaining_installment_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentreceivable',
            name='second_installment_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentreceivable',
            name='second_installment_is_pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentreceivable',
            name='second_installment_is_receieved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentreceivable',
            name='second_installment_is_rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentreceivable',
            name='third_installment_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentreceivable',
            name='third_installment_is_pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentreceivable',
            name='third_installment_is_receieved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentreceivable',
            name='third_installment_is_rejected',
            field=models.BooleanField(default=False),
        ),
    ]