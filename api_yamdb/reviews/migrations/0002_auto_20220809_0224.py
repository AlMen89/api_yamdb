# Generated by Django 2.2.16 on 2022-08-08 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.CharField(max_length=256, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(verbose_name='Год выпуска'),
        ),
    ]