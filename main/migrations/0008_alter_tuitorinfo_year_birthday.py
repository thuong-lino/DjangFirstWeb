# Generated by Django 3.2.3 on 2021-06-02 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210602_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuitorinfo',
            name='year_birthday',
            field=models.CharField(max_length=4, verbose_name='Năm sinh'),
        ),
    ]
