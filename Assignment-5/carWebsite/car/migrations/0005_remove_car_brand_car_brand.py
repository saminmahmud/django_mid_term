# Generated by Django 4.2.7 on 2023-12-15 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_brand_slug'),
        ('car', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.ManyToManyField(to='brand.brand'),
        ),
    ]
