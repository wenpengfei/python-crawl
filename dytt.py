#!/usr/bin/python
"""-"""
from utils.model import Film
from utils.getSoup import get_soup
ROOT_URL = "http://www.dytt8.net"
SOUP = get_soup(ROOT_URL + '/index.htm')
TITLES = SOUP.select_one('.co_area2').select('.co_content2 a')
FILMS = []
for item in TITLES:
    detailUrl = ROOT_URL + item["href"]
    detailSoup = get_soup(detailUrl)
    detailTitle = detailSoup.select_one("div.co_area2 > div.title_all > h1 > font")
    detailImg = detailSoup.select_one("#Zoom img")
    detailDownload = detailSoup.select_one("#Zoom table a")
    if detailImg and detailTitle and detailDownload:
        FILMS.append(
            Film(detailTitle.text,
                 detailImg['src'],
                 '-',
                 detailDownload['href']))
for test in FILMS:
    print test.title
    print test.img_url
    print test.description
    print test.download_url
