import feedparser
import requests
from bs4 import BeautifulSoup as soup



def get_articles():
    url = 'https://kotaku.com/rss'
    p = feedparser.parse(url)
    entries = p['entries']
    for links in entries:
        links = links['link']
        if 'kotaku' in links:
            get_text(links)


def get_text(link):
    print(link)
    source = requests.get(link).text
    page_soup = soup(source, 'html.parser')
    articles = page_soup.find_all('article')
    for article in articles:
        p = article.find('div',{'class':'post-content'}).text
        # text = p.find_all('p')
        print(p)

get_articles()