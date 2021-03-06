# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_id=models.CharField(max_length=120,primary_key=True)
    name=models.CharField(max_length=128)
    created_on=models.DateTimeField(default=datetime.now())

class Answer(models.Model):
    question=models.ForeignKey('Question',  related_name='questions_answer')
    string=models.CharField(max_length=1024)
    username=models.CharField(max_length=128)
    created_on = models.DateTimeField(default=datetime.now())

class Question(models.Model):
    topic=models.ForeignKey(Topic)
    string=models.CharField(max_length=1024)
    username=models.CharField(max_length=128)
    answer=models.ManyToManyField(Answer, related_name='answer_for_question')
    view=models.IntegerField(null=True)
    created_on = models.DateTimeField(default=datetime.now())

class Upvote(models.Model):
    username=models.CharField(max_length=128)
    answer=models.ForeignKey(Answer)
    created_on = models.DateTimeField(default=datetime.now())

class Downvote(models.Model):
    username=models.CharField(max_length=128)
    answer=models.ForeignKey(Answer)
    created_on = models.DateTimeField(default=datetime.now())