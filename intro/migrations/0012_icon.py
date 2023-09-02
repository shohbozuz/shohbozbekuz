# Generated by Django 4.2.4 on 2023-08-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0011_delete_icons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('class_name', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
        ),
    ]
