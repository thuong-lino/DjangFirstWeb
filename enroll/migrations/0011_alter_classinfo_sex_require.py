# Generated by Django 3.2.3 on 2021-06-14 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0010_auto_20210614_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='sex_require',
            field=models.CharField(choices=[(None, 'Yêu cầu về giới tính người dạy'), ('Nam', 'Nam'), ('Nữ', 'Nữ'), ('both', 'Khác')], max_length=10, verbose_name='Yêu cầu về giới tính'),
        ),
    ]