# Generated by Django 3.2.12 on 2022-03-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_auto_20220324_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudhost',
            name='image_id',
            field=models.CharField(max_length=60, null=True, verbose_name='实例镜像'),
        ),
        migrations.AlterField(
            model_name='cloudhost',
            name='instance_charge_type',
            field=models.CharField(max_length=20, null=True, verbose_name='实例计费方式'),
        ),
        migrations.AlterField(
            model_name='cloudhost',
            name='instance_type',
            field=models.CharField(max_length=30, null=True, verbose_name='实例规格'),
        ),
        migrations.AlterField(
            model_name='cloudhost',
            name='instance_type_family',
            field=models.CharField(max_length=20, null=True, verbose_name='实例规格组'),
        ),
        migrations.AlterField(
            model_name='cloudhost',
            name='internet_charge_type',
            field=models.CharField(max_length=20, null=True, verbose_name='公网带宽计费方式'),
        ),
        migrations.AlterField(
            model_name='cloudhost',
            name='resource_group_id',
            field=models.CharField(max_length=30, null=True, verbose_name='资源组'),
        ),
    ]
