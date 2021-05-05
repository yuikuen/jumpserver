# Generated by Django 3.1 on 2021-05-05 08:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0033_user_dingtalk_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('wecom', 'WeCom'), ('email', 'Email'), ('dingtalk', 'DingTalk')], db_index=True, default='', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(default='', max_length=64)),
                ('message', models.CharField(max_length=128, unique=True)),
                ('groups', models.ManyToManyField(related_name='subscriptions', to='users.UserGroup')),
                ('receive_backends', models.ManyToManyField(related_name='subscriptions', to='notifications.Backend')),
                ('users', models.ManyToManyField(related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
