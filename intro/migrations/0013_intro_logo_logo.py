# Generated by Django 4.2.4 on 2023-08-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0012_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='logo_logo',
            field=models.CharField(default='fab fa-dev', max_length=50),
        ),
    ]