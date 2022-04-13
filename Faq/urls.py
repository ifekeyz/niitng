from django.urls import path

from .import views

urlpatterns = [
    path('faq',views.faq, name='faq'),
    # path('about', views.about, name='about'),
]