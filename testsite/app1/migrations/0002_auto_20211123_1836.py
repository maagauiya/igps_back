# Generated by Django 3.2.9 on 2021-11-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app1',
            name='content',
        ),
        migrations.RemoveField(
            model_name='app1',
            name='time_create',
        ),
        migrations.RemoveField(
            model_name='app1',
            name='time_update',
        ),
        migrations.RemoveField(
            model_name='app1',
            name='title',
        ),
        migrations.AddField(
            model_name='app1',
            name='asset_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='app1',
            name='battery_status',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='app1',
            name='current_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='app1',
            name='current_lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='app1',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='app1',
            name='device',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='app1',
            name='is_inzone',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='app1',
            name='user',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]