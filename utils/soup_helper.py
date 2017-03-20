#!/usr/bin/python
"""get_soup"""
import httplib
import urllib2
from bs4 import BeautifulSoup
def get_soup(url, encoding="gbk"):
    """get_soup"""
    try:
        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response, "html.parser", from_encoding=encoding)
        return soup
    except httplib.BadStatusLine:
        pass



    