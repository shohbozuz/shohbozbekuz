# Generated by Django 4.2.4 on 2023-08-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0018_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='mening_rasmim',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]
