from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
#from django.core.context_processors import csrf
from app1.models import *
from django.views.generic.base import TemplateView
import random

list_articles = list(Articles.objects.all())
processedlist = []
for i in range(len(list_articles)):
	j = list_articles[i]
	text = j.text
	finaltext = ' '.join(text.split(' ')[:50])
	j.text = finaltext
	j.source= (Author.objects.filter(source_id=j.source_id)[0]).name
	processedlist.append(j)

def login(request):
    return render(request, 'login.html')

def articles(request):
	if not('articleid' in request.GET):
		return news(request)
	articledet = Articles.objects.filter(article_id=request.GET['articleid'])[0] # fetch article details
	sourcedet = Author.objects.filter(source_id=articledet.source_id)[0] # fetch source details
	relatedpost = list(ArticleSimilarity.objects.filter(article_id=request.GET['articleid'])) #fetch related articles, their url, title, match%
	for i in range(len(relatedpost)):
		relatedpost[i].title = Articles.objects.filter(article_id=relatedpost[i].article_match)[0].title
	return render(request,'article.html',  {'article': articledet, 'relatedposts':relatedpost,'source':sourcedet})

def news(request):
	if not('pagenum' in request.GET):
		return render(request,'news.html',  {'list_articles': processedlist[:10],'pagenum':0})
	elif ('pagenum' in request.GET):
		pagenum = int(request.GET['pagenum'])
		return render(request,'news.html',  {'list_articles': processedlist[pagenum*10:(pagenum+1)*10],'pagenum':pagenum+1})

	# return render(request,"news.html")

def createarticles(request):
	return render(request,'CreateArticle.html')

def handlecreatearticles(request):
	quiz = str(request.GET['quiz'])
	article = str(request.GET['article'])
	article_id_new = len(Articles.objects.all())
	Articles.objects.create(source_id= 0 , link="https://www.thestreet.com/markets/flashback-friday-whats-the-market-smoking--14804612" + str(article_id_new), title = "flashback friday"+str(article_id_new), text=article, agreement_index=0, article_id = article_id_new , number_of_upvotes=0)
	Quiz.objects.create(article_id=article_id_new, quiz = quiz)

	if not('pagenum' in request.GET):
		return render(request,'news.html',  {'list_articles': processedlist[:10],'pagenum':0})
	elif ('pagenum' in request.GET):
		pagenum = int(request.GET['pagenum'])
		return render(request,'news.html',  {'list_articles': processedlist[pagenum*10:(pagenum+1)*10],'pagenum':pagenum+1})

	

def sourcepage(request):
	return render(request,'Sourcepage.html')
