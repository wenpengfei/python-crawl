#!/usr/bin/python
"""module"""
import urllib2
from bs4 import BeautifulSoup
"""ssfsf"""
def getSoup(url, encoding = "gbk"):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response, "html.parser", from_encoding=encoding)
    return soup