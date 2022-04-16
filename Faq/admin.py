from django.contrib import admin

# Register your models here.
from .models import Faq,Client_Question

admin.site.register(Faq)
admin.site.register(Client_Question)