# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-19 13:48
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0005_auto_20160714_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggedArticleReviewEdit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_old_json', django.contrib.postgres.fields.jsonb.JSONField()),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('edit_hash', models.CharField(max_length=20, unique=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleReview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
