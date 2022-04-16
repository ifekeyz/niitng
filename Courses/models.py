from django.db import models
from datetime import datetime

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=100, blank=True)
    posted_by = models.CharField(max_length=100, blank=True)
    posted_time = models.DateTimeField(default = datetime.now, blank=True)
    description = models.TextField(blank=True)
    about_course = models.TextField(blank=True)
    requirement = models.TextField(blank=True)
    is_published = models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.name

class Diploma_Course(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    posted_time = models.DateTimeField(default = datetime.now, blank=True)
    is_published = models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.name

class Curriculum(models.Model):
    title =  models.CharField(max_length=100, blank=True)
    duration = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    posted_time = models.DateTimeField(default = datetime.now, blank=True)
    is_published = models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.title

class Apply_Form(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phoneNo = models.CharField(max_length=100, blank=True)
    branch = models.CharField(max_length=100, blank=True)
    course = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
        
