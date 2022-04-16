from django.db import models 
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    blog = models.CharField(max_length=100, blank=True)
    header = models.CharField(max_length=200, blank=True)
    header2 = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=100, blank=True)
    posted_by = models.CharField(max_length=100, blank=True)
    posted_day = models.CharField(max_length=100, blank=True)
    posted_time = models.DateTimeField(default = datetime.now, blank=True)
    description = models.TextField(blank=True)
    title2 = models.CharField(max_length=100, blank=True)
    more_blog = models.TextField(blank=True)
    title3 = models.CharField(max_length=100, blank=True)
    article = models.TextField(blank=True)
    article2 = models.TextField(blank=True)
    team = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    team_name = models.CharField(max_length=100, blank=True)
    content = models.CharField(max_length=100, blank=True)
    is_published = models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.blog