# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ClothingItem(models.Model):
	model_pic = models.ImageField(upload_to = 'userUploads/', default = 'userUploads/None/no-img.jpg')
    tags =  models.ManyToManyField(Tag)
    pub_date = models.DateTimeField('date added')

class Tag(models.Model):
	tag_text = models.CharField(max_length=30)



#class Choice(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)