# Generated by Django 4.0.6 on 2022-07-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('auther', models.CharField(max_length=70)),
                ('price', models.IntegerField()),
                ('publish_date', models.DateField()),
            ],
        ),
    ]
