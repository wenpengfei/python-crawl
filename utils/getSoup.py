#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
from bs4 import BeautifulSoup
def getSoup(url):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response, "html.parser", from_encoding="gbk")
    return soup