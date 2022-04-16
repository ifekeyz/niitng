from django.contrib import admin

# Register your models here.
from .models import Team,Contact_Us

class TeamAdmin(admin.ModelAdmin):
    list_diaplay = ('id','name','postion')
admin.site.register(Team, TeamAdmin)
admin.site.register(Contact_Us)