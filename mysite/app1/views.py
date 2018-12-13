from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
#from django.core.context_processors import csrf
from app1.models import *
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
	# return  HttpResponse(message)
	articledet = Articles.objects.filter(article_id=request.GET['articleid'])[0] # fetch article details
	sourcedet = Author.objects.filter(source_id=articledet.source_id)[0] # fetch source details
	relatedpost = list(ArticleSimilarity.objects.filter(article_id=request.GET['articleid'])) #fetch related articles, their url, title, match%
	for i in range(len(relatedpost)):
		relatedpost[i].title = Articles.objects.filter(article_id=relatedpost[i].article_match)[0].title
	return render(request,'article.html',  {'article': articledet, 'relatedposts':relatedpost,'source':sourcedet})

def news(request):
    return render(request,'news.html',  {'list_articles': processedlist})

def createarticles(request):
	return render(request,'CreateArticle.html')

def handlecreatearticles(request):
	#val = request.GET['']
	return

def sourcepage(request):

	return render(request,'Sourcepage.html', )
