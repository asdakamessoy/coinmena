# Generated by Django 3.2.3 on 2021-07-01 23:50

from django.db import migrations
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='id',
            field=main.models.ModelBigIntegerAuto(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='currency',
            name='id',
            field=main.models.ModelBigIntegerAuto(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='exchangeratelogs',
            name='id',
            field=main.models.ModelBigIntegerAuto(primary_key=True, serialize=False),
        ),
    ]