from django.db import models

# Create your models here.

class Articles(models.Model):
	source = models.CharField(max_length=30)
	title = models.CharField(max_length=150, primary_key = True)
	text = models.CharField(max_length= 10000)
	link = models.URLField()
	number_of_upvotes = models.IntegerField()

	def __str__(self):

        	return u'%s %s %s %s %s' %  (self.source,self.title,self.text,self.link,self.number_of_upvotes)

class Author(models.Model):
	name = models.CharField(max_length=100)
	reliability_index = models.IntegerField()
	number_of_posts = models.IntegerField()


	def __str__(self):
			return u'%s %s %s ' %  (self.name,self.reliability_index,self.number_of_posts)


class ArticleSimilarity(models.Model):

	article_title = models.CharField(max_length=150)
	article_match = models.CharField(max_length=1000)
	similarity_percentage = models.IntegerField()

	def __str__(self):
			return u'%s %s %s ' %  (self.article_title,self.article_match,self.similarity_percentage)

class Quiz(models.Model):
	article_title = models.CharField(max_length=150)
	quiz = models.CharField(max_length=1000)

	def __str__(self):
			return u'%s %s ' %  (self.article_title,self.quiz)

	 
