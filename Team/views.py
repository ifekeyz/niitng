from django.shortcuts import render
from . models import Team
# Create your views here.

def team(request):
    teams = Team.objects.order_by('position')

    context = {
        'teams':teams
        }
    
    return render(request, 'Pages/team.html', context)