# Generated by Django 4.2.4 on 2023-08-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0024_texnologiya_delete_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texnologiya',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
