# Generated by Django 4.2.4 on 2023-08-30 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0003_intro_rezume_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='logo_text',
            field=models.CharField(default='Shohbozbek', max_length=50),
        ),
    ]
