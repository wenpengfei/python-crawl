#!/usr/bin/python
#coding:utf-8
"""-"""
import re
import sys
from pymongo import MongoClient
from utils.soup_helper import get_soup
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

CLIENT = MongoClient('mongodb://localhost:27017/')
DB = CLIENT.EpicWork
MOVIES = DB.movies

ROOT_URL = "http://pianyuan.net"

def get_year(source):
    """-"""
    re_year = re.findall(r'\((.+?)\)', source)
    if len(re_year) > 0:
        return re_year[0]
    return ''

def get_douban_url(detail_soup):
    """-"""
    detail_soup = detail_soup.find('a', title='豆瓣链接')
    if detail_soup:
        return detail_soup['href']
    return ''

def get_attrs(detail_soup):
    """-"""
    result = []
    attr_names_soup = detail_soup.select('ul.detail strong')
    attr_values_soup = detail_soup.select('ul.detail div')
    attr_values_formatted = []
    for i, val in enumerate(attr_values_soup):
        attr_value_formated_soup = BeautifulSoup(str(val), 'html.parser')
        attr_tags_a = attr_value_formated_soup.find_all('a')
        if len(attr_tags_a) == 0 or len(attr_tags_a) == 1:
            attr_values_formatted.append(attr_value_formated_soup.text)
        else:
            arr_result = []
            for i, val in enumerate(attr_tags_a):
                arr_result.append(val.text)
            attr_values_formatted.append(','.join(arr_result))
    for i, val in enumerate(attr_names_soup):
        result.append({str(val.text): str(attr_values_formatted[i]).strip()})
    return result

HTMLDOC = get_soup('http://pianyuan.net/mv?order=update&p=1')
ITEMSDOCS = HTMLDOC.select('.nopl')

for itemdoc in ITEMSDOCS:
    item_soup = BeautifulSoup(str(itemdoc), 'html.parser')

    SOURCE_URL = ROOT_URL + item_soup.select_one('.thumbnail')['href']
    DETAILSOUP = get_soup(SOURCE_URL)

    movie_title = item_soup.select_one('.nobr').text
    movie_main_actor = item_soup.select_one('.info > p').text
    movie_douban_rate = item_soup.select_one('.sum').text
    movie_img_url = item_soup.select_one('img')['data-original']
    movie_year = get_year(item_soup.select_one('.thumbnail')['title'])
    movie_douban_url = get_douban_url(DETAILSOUP)
    movie_attrs = get_attrs(DETAILSOUP)
    print movie_attrs
