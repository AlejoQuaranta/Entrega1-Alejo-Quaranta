# Generated by Django 4.0.4 on 2022-06-09 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='SKU',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
