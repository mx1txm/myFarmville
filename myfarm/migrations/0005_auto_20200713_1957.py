# Generated by Django 3.0.7 on 2020-07-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfarm', '0004_auto_20200713_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='price_min',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Fruits', 'Veggies'), ('Nuts', 'Honey'), ('Tea', 'Legumes'), ('Oil', 'Wheat'), ('Flowers', 'Mushroom')], default='1', max_length=20),
        ),
    ]
