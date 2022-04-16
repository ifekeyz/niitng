from django.shortcuts import render,redirect
from django.contrib import messages

from Team.models import Team,Contact_Us
from Blog.models import Blog
from Courses.models import Course

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-posted_time')[:3]
    courses = Course.objects.all()[:3]

    context={
        'blogs':blogs,
        'courses':courses
    }
    # 
    if request.method=="POST":
        consulting = Contact_Us()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        consulting.name=name
        consulting.email=email
        consulting.subject=subject
        consulting.message=message
        consulting.save()
        messages.success(request, 'Your request has been submitted')
        return redirect('about')
    return render(request, 'Pages/index.html', context)

def about(request):
    teams = Team.objects.order_by('position').filter(is_mvp=True)[:4]

    context = {
        'teams':teams
        }
    return render(request, 'Pages/about.html', context)