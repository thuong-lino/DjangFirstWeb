# Generated by Django 3.2.3 on 2021-06-12 07:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_classinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuitorinfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tuitorinfo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
