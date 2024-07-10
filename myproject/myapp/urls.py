from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('submissions/', views.submissions_list, name='submissions_list'),
]

