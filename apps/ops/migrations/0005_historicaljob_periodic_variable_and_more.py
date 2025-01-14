# Generated by Django 4.1.13 on 2024-10-30 09:38

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ops', '0004_job_nodes_alter_job_assets'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaljob',
            name='periodic_variable',
            field=models.JSONField(default=dict, verbose_name='Periodic variable'),
        ),
        migrations.AddField(
            model_name='job',
            name='periodic_variable',
            field=models.JSONField(default=dict, verbose_name='Periodic variable'),
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024, null=True, verbose_name='Name')),
                ('var_name', models.CharField(help_text="The variable name used in the script will have a fixed prefix jms_ added to the input variable name. For example, if the input variable name is name, the resulting environment variable will be jms_name, and it can be referenced in the script using {{ jms_name }}", max_length=1024, null=True, verbose_name='Variable name')),
                ('default_value', models.CharField(max_length=2048, null=True, verbose_name='Default Value')),
                ('type', models.CharField(default='text', max_length=64, verbose_name='Variable type')),
                ('tips', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Tips')),
                ('required', models.BooleanField(default=False, verbose_name='Required')),
                ('extra_args', models.JSONField(default=dict, verbose_name='ExtraVars')),
                ('adhoc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variable', to='ops.adhoc', verbose_name='Adhoc')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variable', to='ops.job', verbose_name='Job')),
                ('playbook', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variable', to='ops.playbook', verbose_name='Playbook')),
            ],
            options={
                'verbose_name': 'Variable',
                'ordering': ['date_created'],
            },
        ),
    ]
