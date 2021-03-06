# Generated by Django 3.2.9 on 2021-12-09 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20211123_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esn', models.CharField(blank=True, max_length=10, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStamp', models.DateTimeField()),
                ('messageID', models.CharField(blank=True, max_length=50, null=True)),
                ('esn', models.CharField(blank=True, max_length=10, null=True)),
                ('unixTime', models.CharField(blank=True, max_length=10, null=True)),
                ('gps', models.CharField(blank=True, max_length=10, null=True)),
                ('payload', models.CharField(blank=True, max_length=30, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device', to='app1.devices')),
            ],
        ),
    ]
