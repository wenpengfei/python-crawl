#!/usr/bin/python
# -*- coding: UTF-8 -*-
from utils.model import Film
from utils.getSoup import getSoup

rootUrl = "http://www.dytt8.net"

soup = getSoup(rootUrl + '/index.html')
titles = soup.select_one('.co_area2').select('.co_content2 a')
films = []
for item in titles:
    detailUrl = rootUrl+item["href"]
    detailSoup = getSoup(detailUrl)
    detailTitle = detailSoup.select_one("div.co_area2 > div.title_all > h1 > font")
    detailImg = detailSoup.select_one("#Zoom img")
    detailDownload = detailSoup.select_one("#Zoom table a")
    if detailImg and detailTitle and detailDownload:
        films.append(Film(detailTitle.text, detailImg['src'], '-', detailDownload['href']))
for test in films:
    print test.title
    print test.imgUrl
    print test.description
    print test.downloadUrl
