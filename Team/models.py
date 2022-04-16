from turtle import position
from django.db import models
from datetime import datetime

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    listingDate = models.DateTimeField(default = datetime.now, blank=True)
    is_mvp =  models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name



class Contact_Us(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name



