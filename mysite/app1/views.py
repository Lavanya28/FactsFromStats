from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
#from django.core.context_processors import csrf
from app1.models import Articles
from django.views.generic.base import TemplateView


list_articles = Articles.objects.all()
def index(request):
    return render(request, 'login.html')

def articles(request):
	if 'q' in request.GET:
		message = 'You searched for: %r' % request.GET['q']
	return  HttpResponse(message)

def news(request):
    return render(request,'news.html',  {'list_articles': list_articles})
