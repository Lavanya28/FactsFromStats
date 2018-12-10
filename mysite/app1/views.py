from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
#from django.core.context_processors import csrf
from app1.models import Articles
from django.views.generic.base import TemplateView

def index(request):
    return render(request, 'news.html')

def articles(request):
    list_articles = Articles.objects.all()
    return  HttpResponse(list_articles[0])

def news(request):
	
    return render(request,'news.html')
