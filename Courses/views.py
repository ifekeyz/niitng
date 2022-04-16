from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Course,Diploma_Course

def courses(request):
    courses = Course.objects.all()
    diplomas = Diploma_Course.objects.all()

    context={
        'courses':courses,
        'diplomas':diplomas,
    }
    return render(request,'Pages/courses.html', context)


def course(request,course_id):
    courses = Course.objects.all()[:4]
    course = get_object_or_404(Course, pk=course_id)

    context={
        'course':course,
        'courses':courses,
        
    }
    return render(request,'Pages/single_course.html', context)