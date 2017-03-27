#!/usr/bin/python
#coding:utf-8
"""-"""
import re
import sys
from pymongo import MongoClient
from utils.soup_helper import get_soup

reload(sys)
sys.setdefaultencoding('utf8')

CLIENT = MongoClient('mongodb://localhost:27017/')
DB = CLIENT.EpicWork
MOVIES = DB.movies

ROOT_URL = "http://www.dytt8.net"
SOUP = get_soup(ROOT_URL + '/index.htm')
TITLES = SOUP.select_one('.co_area2').select('.co_content2 a')
FILMS = []
for item in TITLES:
    detailUrl = ROOT_URL + item["href"]
    detailSoup = get_soup(detailUrl)
    if detailSoup is not None:
        detailTitle = detailSoup.select_one(
            "div.co_area2 > div.title_all > h1 > font"
            )
        detailImg = detailSoup.select_one("#Zoom img")
        detailDownload = detailSoup.select_one("#Zoom table a")
        if detailImg and detailTitle and detailDownload:
            originFilmTitle = detailTitle.text
            print 'originFilmTitle'
            print str(originFilmTitle)
            print '=============================='
            filmTitle = ""
            filmImg = detailImg['src']
            filmDownload = detailDownload['href']

            idx = originFilmTitle.find("《")
            if idx != -1:
                filmTitle = re.findall("《(.+?)》", str(originFilmTitle))[0]
            else:
                filmTitle = originFilmTitle
            FILMS.append(
                {
                    "originFilmTitle":originFilmTitle,
                    "filmTitle":filmTitle,
                    "filmImg":filmImg,
                    "filmDownload":filmDownload
                })
        for test in FILMS:
            print filmTitle
            print filmImg
            print originFilmTitle
            print filmDownload
RESULT = MOVIES.insert_many(FILMS)
print RESULT
