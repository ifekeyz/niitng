from django.shortcuts import redirect, render

# Create your views here.
def faq(request):
    return render(request,'Pages/Faq.html')