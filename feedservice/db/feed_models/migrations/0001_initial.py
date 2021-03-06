# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-18 10:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(max_length=1024)),
                ('username', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 10, 44, 47, 809490))),
            ],
        ),
        migrations.CreateModel(
            name='Downvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 10, 44, 47, 813227))),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed_models.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(max_length=1024)),
                ('username', models.CharField(max_length=128)),
                ('view', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 10, 44, 47, 810412))),
                ('answer', models.ManyToManyField(related_name='answer_for_question', to='feed_models.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 10, 44, 47, 808763))),
            ],
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 10, 44, 47, 812456))),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed_models.Answer')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed_models.Topic'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_answer', to='feed_models.Question'),
        ),
    ]
