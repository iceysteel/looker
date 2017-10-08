# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Create your models here.

class Tag(models.Model):
	tag_text = models.CharField(max_length=30)

class ClothingItem(models.Model):
	model_pic = models.ImageField(upload_to = 'userUploads/', default = 'userUploads/None/no-img.jpg')
	tags =  models.ManyToManyField(Tag)
	pub_date = models.DateTimeField('date added')
	#bottom top or shoes?
	item_type = models.TextField(max_length=20,blank=True); 
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)




#class Choice(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)