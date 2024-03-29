# Generated by Django 3.2.2 on 2021-05-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Пиццерия')),
                ('description', models.TextField(verbose_name='Описание')),
                ('rating', models.FloatField(default=0, verbose_name='Рейтинг')),
                ('url', models.URLField(verbose_name='Интернет-адрес пиццерии')),
            ],
        ),
    ]
