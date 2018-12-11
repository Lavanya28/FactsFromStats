
import os
import sys
import pickle 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)
from app1.models import Articles, Author, ArticleSimilarity, Quiz 

with open('cleanedarticles.pickle', 'rb') as f: 
	obj = pickle.load(f)

with open('articlessimilarity.pickle','rb') as f:
	obj_sim = pickle.load(f)

#print (obj_sim[4])
with open ('sourcereliability.pickle', 'rb') as f:
	obj_source = pickle.load(f)

#print (obj[0][0])source 
#print (obj[0][1])link
#print (obj[0][2])title 
#print (obj[3][4])
a
#list1 = [["cnn", "title 1", "text 1" , "url 1", 8 ] , ["cnn", "title 2", "text 2" , "url 2", 8 ] , ["bbc", "title 3", "text 3" , "url 3", 8 ], ["fox", "title 4", "text 4" , "url 4", 8 ] ] 

#list2 = [ ["cnn", 4, 34], ["cnn", 4, 34], ["cnn", 4, 34] ,["cnn", 4, 34] ]

#list3 = [ ["title 1", "title 2", 6], ["title 2", "title 3", 4] , ["title 1", "title 4", 6]]

list4 = [["title 1", "quiz 1"], ["title 1", "quiz 1"] , ["title 1", "quiz 1"], ["title 1", "quiz 1"]]

#populate Articles table: source title text link number_of_upvotes


for ele in obj:
	try:
		Articles.objects.create(source = ele[0], title = ele[2], text=ele[3], link=ele[1], number_of_upvotes=ele[4])
	except:
		continue 

#populate Author table: name reliability_index number_of_posts

for ele in obj_source:
	try:
		Author.objects.create(name=ele[0], reliability_index=ele[1], number_of_posts= 21)
	except:
		continue 

#populate ArticleSimilarity table: article_title article_match similarity_percentage
for ele in obj_sim:
	try:
		ArticleSimilarity.objects.create(article_title=ele[0], article_match=ele[1], similarity_percentage= 3)
	except:
		continue

#populate Quiz table: article_title quiz
for ele in list4:
	try:
		Quiz.objects.create(article_title=ele[0], quiz=ele[1])
	except:
		continue


		