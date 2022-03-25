# Generated by Django 3.2.12 on 2022-03-24 07:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecs',
            name='public_ipaddress',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True, verbose_name='公网 ip'),
        ),
        migrations.AlterField(
            model_name='ecs',
            name='creation_time',
            field=models.DateTimeField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='ecs',
            name='expired_time',
            field=models.DateTimeField(verbose_name='过期时间'),
        ),
    ]