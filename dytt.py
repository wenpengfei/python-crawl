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
        detailInfo = detailSoup.select_one("#Zoom p")
        if detailImg and detailTitle and detailDownload:
            originFilmTitle = detailTitle.text
            filmTitle = ""
            filmImg = detailImg['src']
            filmDownload = detailDownload['href']

            # douban_detailUrl = ''
            # douban_rate = re.findall("◎导　　演(.+?)<br />", str(originFilmTitle))
            # douban_director = re.findall("◎导　　演(.+?)<br />", str(originFilmTitle))
            # douban_screenwriter = re.findall("◎导　　演(.+?)<br />", str(originFilmTitle))
            # douban_actor = re.findall("◎导　　演(.+?)<br />", str(originFilmTitle))
            # douban_genre = re.findall("◎导　　演(.+?)<br />", str(originFilmTitle))
            # douban_country = re.findall("◎导　　演(.+?)<br />", str(originFilmTitle))
            # douban_language = re.findall("◎导　　演(.+?)<br />", str(originFilmTitle))
            # douban_releaseDate = re.findall("◎导　　演(.+?)<br />", str(originFilmTitle))
            # douban_runtime = re.findall("◎导　　演(.+?)<br />", str(originFilmTitle))
            # douban_imdbUrl = re.findall("◎导　　演(.+?)<br />", str(originFilmTitle))
            # imdb_rate = re.findall("◎导　　演(.+?)<br />", str(originFilmTitle))

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
                    "filmDownload":filmDownload,
                    "releaseDate": dytt_releaseDate,
                    "genre": dytt_genre,
                    "director": dytt_director,
                    "actor": dytt_actor,
                })
RESULT = MOVIES.insert_many(FILMS)
print RESULT
        # for test in FILMS:
        #     print filmTitle
        #     print filmImg
        #     print originFilmTitle
        #     print filmDownload


# def getDyttDetail(regexp, source):
#     return re.findall(regexp, str(source)[0]
