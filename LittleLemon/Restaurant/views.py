from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def sayhello(request):
    return HttpResponse("Hello Django!")


def index(request):
    return render(request, 'index.html')
