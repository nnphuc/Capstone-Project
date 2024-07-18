from django.urls import path, include

from . import views

urlpatterns = [
    path('hello', views.sayhello, name='sayhello'),
    path('', views.index, name='index'),
]