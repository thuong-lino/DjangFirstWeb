# Generated by Django 3.2.3 on 2021-06-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_alter_classinfo_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='fee_expected',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Mức lương'),
        ),
    ]
