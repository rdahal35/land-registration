# Generated by Django 3.1.7 on 2021-03-08 12:38

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=250, verbose_name='Full Name')),
                ('address', models.CharField(max_length=250, verbose_name='Address')),
                ('contact_no', models.CharField(max_length=250, verbose_name='Contact Number')),
                ('coordinate', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=15)),
                ('area', models.FloatField(max_length=50, verbose_name='Area in Sqr ft')),
                ('floor_numbers', models.IntegerField(blank=True, null=True, verbose_name='Number of floors')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Propertys',
            },
        ),
    ]