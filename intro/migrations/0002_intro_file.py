# Generated by Django 4.2.4 on 2023-08-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='file',
            field=models.FileField(default='default_resume.pdf', upload_to='resumes/'),
        ),
    ]
