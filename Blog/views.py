from django.shortcuts import get_object_or_404, render
from .models import Blog
# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()

    context={
        'blogs':blogs
    }
    return render(request, 'Pages/blog.html',context)

def blog(request,blog_id):
    blogs = Blog.objects.all()[:4]
    blog = get_object_or_404(Blog, pk=blog_id)

    context={
        'blog':blog,
        'blogs':blogs,
        
    }
    return render(request,'Pages/single_blog.html', context)