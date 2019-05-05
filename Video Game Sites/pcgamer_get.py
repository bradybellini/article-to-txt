import feedparser
import requests
import os
import datetime
from bs4 import BeautifulSoup as soup

def get_articles():
    url = 'https://www.pcgamer.com/rss'
    p = feedparser.parse(url)
    for entry in p.entries:
        try:
            author = entry.author
        except:
            author = 'no author specified'
        title = entry.title
        link = entry.link
        pub_date = entry.published
        if 'pcgamer' in link:
            get_text(link, author, title, pub_date)

def get_text(link, author, title, pub_date):
    source = requests.get(link).text
    page_soup = soup(source, 'html.parser')
    articles = page_soup.find_all('content-wrapper')
    for article in articles:
        p = article.find('div',{'id':'article-body'}).text
        write_to_file(title, pub_date, author, link, p)

def write_to_file(title, pub_date, author, link, p):
    time = datetime.datetime.now()
    write_title = title + " - " + pub_date + '.txt'
    title_date = time.strftime('_%m-%d-%y')
    cwd = 'Pcgamer' + title_date
    try:
        if not os.path.exists(cwd):
            os.makedirs(cwd)
        write_path = cwd + '/ ' + write_title
    except:
        pass
    try:
        f = open(write_path, 'w+')
        f.write('Title: ' + title + '\n' 
                'Author: ' + author + '\n'  
                'Original Link: ' + link + '\n'
                'Published: ' + pub_date + '\n'
                'Article: ' + p )
    except:
        pass

get_articles()