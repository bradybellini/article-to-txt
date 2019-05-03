import feedparser
import requests
from bs4 import BeautifulSoup as soup



def get_articles():
    url = 'https://kotaku.com/rss'
    p = feedparser.parse(url)
    for entry in p.entries:
        author = entry.author
        title = entry.title
        link = entry.link
        pub_date = entry.published
        if 'kotaku' in link:
            get_text(link, author, title, pub_date)


def get_text(link, author, title, pub_date):
    source = requests.get(link).text
    page_soup = soup(source, 'html.parser')
    articles = page_soup.find_all('article')
    for article in articles:
        p = article.find('div',{'class':'post-content'}).text
        write_to_file(title, pub_date, author, link, p)

def write_to_file(title, pub_date, author, link, p):
    write_title = title + "-" + pub_date
    f = open(write_title, 'w+')
    f.write('Title: ' + title + '\n' 
            'Author: ' + author + '\n'  
            'Original Link: ' + link + '\n'
            'Published: ' + pub_date + '\n'
            'Article: ' + p )

get_articles()