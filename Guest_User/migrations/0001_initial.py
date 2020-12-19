# Generated by Django 3.0.8 on 2020-09-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('EMail', models.CharField(max_length=300)),
                ('Mobile', models.CharField(max_length=100, null=True)),
                ('Service', models.CharField(max_length=100)),
                ('Need', models.CharField(max_length=200, null=True)),
                ('Language', models.CharField(max_length=200, null=True)),
                ('Description', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
