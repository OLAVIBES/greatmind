# Generated by Django 4.1.7 on 2023-03-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='amount',
            field=models.CharField(max_length=10),
        ),
    ]
