# Generated by Django 4.2.4 on 2023-09-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0027_delete_texnologiya'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('skill_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
