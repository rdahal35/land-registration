# Generated by Django 3.1 on 2022-02-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0003_property_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='survey_no',
            field=models.IntegerField(blank=True, null=True, verbose_name='Survey Number'),
        ),
    ]
