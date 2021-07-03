# Generated by Django 3.2.3 on 2021-07-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pk_change'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exchangeratelogs',
            name='code',
        ),
        migrations.RemoveField(
            model_name='exchangeratelogs',
            name='name',
        ),
        migrations.AddField(
            model_name='exchangeratelogs',
            name='exchange_rate',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='exchangeratelogs',
            name='message',
            field=models.TextField(blank=True, help_text='Response/error message can be saved here'),
        ),
    ]