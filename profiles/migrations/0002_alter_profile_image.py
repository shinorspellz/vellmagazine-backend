# Generated by Django 4.1.7 on 2023-03-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../profile_avatar_e38sd0', upload_to='images/'),
        ),
    ]
