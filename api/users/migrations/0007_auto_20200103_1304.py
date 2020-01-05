# Generated by Django 3.0.1 on 2020-01-03 05:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200102_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCodeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='邮箱')),
                ('code', models.CharField(max_length=10, verbose_name='验证码')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '邮件验证码',
                'verbose_name_plural': '邮件验证码',
            },
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别'),
        ),
    ]