from django.contrib import messages
from django.shortcuts import redirect, render

from Faq.models import Faq,Client_Question
from Blog.models import Blog
# Create your views here.
def faq(request):
    faqs = Faq.objects.all()
    blogs = Blog.objects.order_by('-posted_time')[:3]

    context={
        'faqs':faqs,
        'blogs':blogs
    }

    if request.method=="POST":
        consulting = Client_Question()
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

    return render(request,'Pages/Faq.html', context)