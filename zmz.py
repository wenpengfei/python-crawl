#!/usr/bin/python
"""main"""
from utils.model import Film
from utils.getSoup import getSoup

ROOT_URL = "http://www.zmz2017.com/"
FILMS = []
SOUP = getSoup(ROOT_URL)
HOTS = SOUP.select_one(".box.clearfix").select("li a")
for hot in HOTS:
    if hot and hot.text:
        FILMS.append(Film(hot.text, '-', '-', '-'))
for test in FILMS:
    print test.title
    print test.imgUrl
    print test.description
    print test.downloadUrl

