from django.db import models

# Create your models here.

class Articles(models.Model):
	article_id = models.IntegerField()
	source_id = models.IntegerField()
	title = models.CharField(max_length=150, primary_key = True)
	text = models.CharField(max_length= 10000)
	link = models.URLField()
	number_of_upvotes = models.IntegerField()
	agreement_index=models.FloatField()

	def __str__(self):

        	return u'%s %s %s %s %s %s %s' %  (self.article_id, self.source_id,self.title,self.text,self.link,self.number_of_upvotes,self.agreement_index)

class Author(models.Model):
	source_id = models.IntegerField()
	name = models.CharField(max_length=100)
	reliability_index = models.FloatField()
	number_of_posts = models.IntegerField()


	def __str__(self):
			return u'%s %s %s %s ' %  (self.source_id ,self.name,self.reliability_index,self.number_of_posts)


class ArticleSimilarity(models.Model):

	article_id = models.IntegerField()
	article_match = models.IntegerField()
	similarity_percentage = models.FloatField()

	def __str__(self):
			return u'%s %s %s ' %  (self.article_id,self.article_match,self.similarity_percentage)

class Quiz(models.Model):
	article_id = models.IntegerField()
	quiz = models.CharField(max_length=1000)

	def __str__(self):
			return u'%s %s ' %  (self.article_id,self.quiz)

	 
