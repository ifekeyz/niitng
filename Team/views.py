from django.shortcuts import render

# Create your views here.

def team(request):
    return render(request, 'Pages/team.html')