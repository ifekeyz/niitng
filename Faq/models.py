from django.db import models
from datetime import datetime

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=100, blank=True)
    answer = models.TextField(blank=True)
    posted_time = models.DateTimeField(default = datetime.now, blank=True)
    is_published = models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.question

class Client_Question(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.subject