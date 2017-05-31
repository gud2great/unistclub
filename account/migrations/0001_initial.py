# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-29 04:46
from __future__ import unicode_literals

import account.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UcUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('login_id', models.CharField(max_length=16, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('is_admin', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('type', models.CharField(choices=[('defualt', '미인증'), ('student', '인증'), ('company', '업자')], max_length=15)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, height_field='height', null=True, upload_to='', width_field='width')),
                ('major', models.CharField(max_length=30)),
                ('minor', models.CharField(max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', account.managers.UcUserManager()),
            ],
        ),
    ]