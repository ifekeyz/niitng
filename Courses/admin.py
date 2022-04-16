from django.contrib import admin

# Register your models here.
from .models import Course,Curriculum,Diploma_Course,Apply_Form

admin.site.register(Course)
admin.site.register(Curriculum)
admin.site.register(Diploma_Course)
admin.site.register(Apply_Form)