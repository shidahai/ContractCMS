# Generated by Django 2.2.7 on 2020-04-21 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0011_contract_is_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
    ]
