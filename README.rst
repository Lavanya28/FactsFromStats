The project files can be classified into WebScraping, Similarity computation in Articles and the Web Framework. 
&nbsp;
Web Scraping:
Tools & Installations required:

beautifulsoup4>=4.4.1
Pillow>=3.3.0
PyYAML>=3.11
cssselect>=0.9.2
lxml>=3.6.0
nltk>=3.2.1
requests>=2.10.0
feedparser>=5.2.1
tldextract>=2.0.1
feedfinder2>=0.0.4
jieba3k>=0.35.1
python-dateutil>=2.5.3
tinysegmenter==0.3 

The file NewsScraper.py is the article scraper and websites can be added to NewsPapers.json. The variable LIMIT can be edited to change the number of articles scraped from each website. 
The json files can also be fed with RSS links that provide more consistent data for scraping. 

Similarity computation:
Once we have all the articles saved in the articles.pickle file, we can run the SentenceSimilarity.ipynb notebook which will preprocess the data, compute related posts and then compute the sentences that match the sentiment and then get the agreement index.
All these will be stored in pickle files inside the mysite folder which will be used by the django to create the database:
1. cleanedarticles.pickle
2. sourcereliability.pickle
3. articlessimilarity.pickle

Website:
The pickle files will be used to populate the database. Simply run python populate_db.py to populate all tables of the database. 

The webframework runs using django, run the following command inside SocialSpaces/mysite to view the site:
python manage.py runserver 






