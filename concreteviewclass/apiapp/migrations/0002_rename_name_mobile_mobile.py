# Generated by Django 4.0.6 on 2022-07-28 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobile',
            old_name='name',
            new_name='mobile',
        ),
    ]
