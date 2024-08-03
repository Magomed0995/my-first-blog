from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html', {})
# Create your views here.

def categ(request):
    return HttpResponse('<h1>page1</h1>')