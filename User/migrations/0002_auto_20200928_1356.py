# Generated by Django 3.0.8 on 2020-09-28 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_login',
            name='Mobile',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user_login',
            name='Pin',
            field=models.CharField(max_length=20),
        ),
    ]
