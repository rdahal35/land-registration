# Generated by Django 3.1.7 on 2021-03-08 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0003_auto_20210308_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('LA', 'Land'), ('HO', 'House')], default='HO', max_length=2, verbose_name='Property Type'),
        ),
    ]