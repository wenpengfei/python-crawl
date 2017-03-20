#!/usr/bin/python
"""-"""
from pymongo import MongoClient
from utils.model import Film
from utils.soup_helper import get_soup

client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
posts = db.posts

ROOT_URL = "http://www.dytt8.net"
SOUP = get_soup(ROOT_URL + '/index.htm')
TITLES = SOUP.select_one('.co_area2').select('.co_content2 a')
FILMS = []
try:
    for item in TITLES:
        detailUrl = ROOT_URL + item["href"]
        detailSoup = get_soup(detailUrl)
        if detailSoup is not None:
            detailTitle = detailSoup.select_one("div.co_area2 > div.title_all > h1 > font")
            detailImg = detailSoup.select_one("#Zoom img")
            detailDownload = detailSoup.select_one("#Zoom table a")
            if detailImg and detailTitle and detailDownload:
                filmTitle = detailTitle.text
                filmImg = detailImg['src']
                filmDownload = detailDownload['href']
                FILMS.append({"filmTitle":filmTitle,"filmImg":filmImg,"filmDownload":filmDownload})
            # for test in FILMS:
            #     print test.title
            #     print test.img_url
            #     print test.description
            #     print test.download_url
    result = posts.insert_many(FILMS)
    print result
except Exception, e:
    print e.message
    pass
