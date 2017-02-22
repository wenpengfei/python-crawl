#!/usr/bin/python
"""main"""
from utils.model import Film
from utils.getSoup import getSoup

ROOT_URL = "http://www.dytt8.net"

SOUP = getSoup(ROOT_URL + '/index.htm')
TITLES = SOUP.select_one('.co_area2').select('.co_content2 a')
FILMS = []
for item in TITLES:
    detailUrl = ROOT_URL + item["href"]
    detailSoup = getSoup(detailUrl)
    detailTitle = detailSoup.select_one("div.co_area2 > div.title_all > h1 > font")
    detailImg = detailSoup.select_one("#Zoom img")
    detailDownload = detailSoup.select_one("#Zoom table a")
    if detailImg and detailTitle and detailDownload:
        FILMS.append(Film(detailTitle.text, detailImg['src'], '-', detailDownload['href']))
for test in FILMS:
    print test.title
    print test.imgUrl
    print test.description
    print test.downloadUrl
