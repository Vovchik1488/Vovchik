# Generated by Django 3.2.2 on 2021-05-07 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0002_pizza'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name': 'Пицца', 'verbose_name_plural': 'Пиццы'},
        ),
        migrations.AlterModelOptions(
            name='pizzashop',
            options={'verbose_name': 'Пиццерия', 'verbose_name_plural': 'Пиццерии'},
        ),
        migrations.AlterField(
            model_name='pizza',
            name='pizzashop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.pizzashop', verbose_name='Пицца'),
        ),
    ]
