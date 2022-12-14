# Generated by Django 3.0.2 on 2020-05-06 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200505_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='QQLoginTokenModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=32, verbose_name='授权令牌')),
                ('expires_in', models.IntegerField(verbose_name='授权令牌的有效期，单位为秒')),
                ('refresh_token', models.CharField(max_length=32, verbose_name='授权续期需要提供的参数')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='qq_login', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': 'QQ登陆TOKEN',
                'verbose_name_plural': 'QQ登陆TOKEN',
            },
        ),
    ]
