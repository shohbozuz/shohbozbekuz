# Generated by Django 4.2.4 on 2023-08-30 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0009_remove_intro_icon_remove_intro_linkedin_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(default='fab fa-linkedin', max_length=50)),
                ('icon_url', models.TextField(default='https://www.linkedin.com/in/jigar-sable/')),
            ],
        ),
    ]
