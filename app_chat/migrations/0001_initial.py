# Generated by Django 5.0.6 on 2024-08-16 06:12

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroup',
            fields=[
                ('uid', models.CharField(default=uuid.uuid4, editable=False, max_length=500, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('group_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('room_no', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupMessage',
            fields=[
                ('uid', models.CharField(default=uuid.uuid4, editable=False, max_length=500, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_chat.chatgroup')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
