# Generated by Django 2.1.1 on 2018-11-14 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20181114_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='rate',
            field=models.DecimalField(decimal_places=4, max_digits=6, verbose_name='增值税率'),
        ),
    ]