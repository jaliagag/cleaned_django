# Generated by Django 4.0.4 on 2022-06-19 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookRecord', '0003_dev'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='test',
        ),
    ]
