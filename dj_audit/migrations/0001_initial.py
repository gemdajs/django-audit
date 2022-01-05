# Generated by Django 3.2.8 on 2021-10-24 15:27

from django import __version__
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

if __version__ > '2.2':
    from django.db.models import JSONField
else:
    from django.contrib.postgres.fields import JSONField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.BigAutoField(primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(
                    null=True, verbose_name='IP Address')),
                ('host_name', models.CharField(default='',
                 max_length=200, verbose_name='Host Name')),
                ('content_type', models.CharField(
                    max_length=200, verbose_name='Content Type')),
                ('query_string', models.TextField(verbose_name='Query String')),
                ('post_data', JSONField(blank=True,
                 null=True, verbose_name='Post Data')),
                ('http_method', models.CharField(
                    max_length=20, verbose_name='HTTP Method')),
                ('http_referer', models.CharField(
                    max_length=500, verbose_name='HTTP Method')),
                ('path_info', models.CharField(max_length=255, verbose_name='Path')),
                ('request_data', models.TextField(null=True)),
                ('response_status_code', models.IntegerField(null=True)),
                ('response_reason_phrase', models.TextField()),
                ('response_body', JSONField(default='')),
                ('attempt_time', models.DateTimeField(auto_now_add=True)),
                ('response_time', models.DateTimeField(blank=True, null=True)),
                ('log_status', models.CharField(choices=[('success', 'success'), (
                    'failed', 'failed'), ('warning', 'warning')], default='success', max_length=20)),
                ('response_type', models.CharField(choices=[
                 ('http', 'http'), ('rest', 'rest')], default='http', max_length=20)),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-attempt_time'],
            },
        ),
    ]
