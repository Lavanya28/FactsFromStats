from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
#from django.core.context_processors import csrf
from app1.models import Articles
from django.views.generic.base import TemplateView


list_articles = Articles.objects.all()[:10]
processedlist = []
for i in range(len(list_articles)):
	j = list_articles[i]
	text = j.text
	finaltext = ' '.join(text.split(' ')[:50])
	j.text = finaltext
	processedlist.append(j)



def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'login.html')

def articles(request):
	if 'articleid' in request.GET:
		message = 'You searched for: %r' % request.GET['articleid']
	return  HttpResponse(message)
	articledet = 0 # fetch article details
	sourcedet = 0 # fetch source details
	relatedpost = 0 #fetch related articles, their url, title, match%
	return render(request,'article.html',  {'article': articledet, 'relatedposts':relatedpost,'source':sourcedet})

def news(request):
    return render(request,'news.html',  {'list_articles': processedlist})
