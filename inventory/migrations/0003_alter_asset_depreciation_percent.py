# Generated by Django 4.0.4 on 2022-05-29 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_asset_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='depreciation_percent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]