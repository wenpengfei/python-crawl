#!/usr/bin/python
"""-"""
from utils.model import Film
from utils.soup_helper import get_soup

ROOT_URL = "http://www.zmz2017.com/"
FILMS = []
SOUP = get_soup(ROOT_URL)
HOTS = SOUP.select_one(".box.clearfix").select("li a")
for hot in HOTS:
    if hot and hot.text:
        FILMS.append(Film(hot.text, '-', '-', '-'))
for test in FILMS:
    print test.title
    print test.img_url
    print test.description
    print test.download_url

