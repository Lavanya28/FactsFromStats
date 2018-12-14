from django.shortcuts import render
import math
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
	j.text =  ' '.join(j.text.split(' ')[:50])
	j.source= (Author.objects.filter(source_id=j.source_id)[0]).name
	processedlist.append(j)

def login(request):
    return render(request, 'login.html')

def articles(request):
	if('upvote' in request.GET and 'articleid' in request.GET):
		upv =request.GET['upvote']
		aid=request.GET['articleid']
		a=Articles.objects.filter(article_id = int(aid))[0]
		if(upv=="1"):
			a.number_of_upvotes=a.number_of_upvotes+1
			a.save()
		else:
			a.number_of_upvotes=a.number_of_upvotes-1
			a.save()

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
	else:
		pagenum = int(request.GET['pagenum'])
		return render(request,'news.html',  {'list_articles': processedlist[pagenum*10:(pagenum+1)*10],'pagenum':pagenum+1})
	# return render(request,"news.html")

def createarticles(request):
	return render(request,'CreateArticle.html')

def handlecreatearticles(request):
	
	article = str(request.GET['article'])
	title=str(request.GET['title'])
	article_id_new = len(Articles.objects.all())
	Articles.objects.create(source_id= 0 , link="https://www.thestreet.com/markets/flashback-friday-whats-the-market-smoking--14804612" + str(article_id_new), title = title +str(article_id_new), text=article, agreement_index=5, article_id = article_id_new , number_of_upvotes=0)
	

	if not('pagenum' in request.GET):
		return render(request,'news.html',  {'list_articles': processedlist[:10],'pagenum':0})
	elif ('pagenum' in request.GET):
		pagenum = int(request.GET['pagenum'])
		return render(request,'news.html',  {'list_articles': processedlist[pagenum*10:(pagenum+1)*10],'pagenum':pagenum+1})

	
def upvoting(request):
	a=request.GET['upvote']
	sourcename=request.GET['sourcename']
	if(a=="1"):
		author = Author.objects.filter(name= sourcename)[0]
		reliability = author.reliability_index
		new_reliability = reliability + math.log(1+1/author.number_of_posts)
		if(new_reliability>10):
			new_reliability=10
		author.reliability_index = new_reliability
		author.save()
	else:
		author = Author.objects.filter(name= sourcename)[0]
		reliability = author.reliability_index
		new_reliability = reliability - math.log(1+1/author.number_of_posts)
		if(new_reliability<0):
			new_reliability=0
		author.reliability_index = new_reliability
		author.save()
	sourceid = Author.objects.filter(name=sourcename)
	reliabilityindex = sourceid[0].reliability_index
	#print (sourceid)
	
	list_articles = list(Articles.objects.filter(source_id=sourceid[0].source_id))
	processedlist = []
	for i in range(len(list_articles)):
		j = list_articles[i]
		j.text =  ' '.join(j.text.split(' ')[:50])
		j.source= (Author.objects.filter(source_id=j.source_id)[0]).name
		processedlist.append(j)

	return render(request,'Sourcepage.html', {'sourcename': sourcename, 'list_articles': processedlist, 'reliabilityindex':reliabilityindex })


def sourcepage(request):
	sourcename = request.GET['sourcename']
	sourceid = Author.objects.filter(name=sourcename)
	reliabilityindex = sourceid[0].reliability_index
	#print (sourceid)

	list_articles = list(Articles.objects.filter(source_id=sourceid[0].source_id))
	processedlist = []
	for i in range(len(list_articles)):
		j = list_articles[i]
		j.text =  ' '.join(j.text.split(' ')[:50])
		j.source= (Author.objects.filter(source_id=j.source_id)[0]).name
		processedlist.append(j)

	return render(request,'Sourcepage.html', {'sourcename': sourcename, 'list_articles': processedlist, 'reliabilityindex':reliabilityindex })
