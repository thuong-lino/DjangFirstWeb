# Generated by Django 3.2.3 on 2021-06-01 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_class_info_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_info',
            name='sex_require',
            field=models.CharField(choices=[('Male', 'Nam'), ('Female', 'Nữ')], default='Male', max_length=10),
        ),
    ]
