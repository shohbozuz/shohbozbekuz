# Generated by Django 4.2.4 on 2023-08-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0019_about_mening_rasmim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='mening_rasmim',
            field=models.ImageField(upload_to='image/'),
        ),
    ]