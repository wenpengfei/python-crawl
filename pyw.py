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
HTMLDOC = get_soup('http://pianyuan.net/mv?type=1&order=update&p=1')
ITEMSDOCS = HTMLDOC.select('.nopl')

def get_year(source):
    """-"""
    re_year = re.findall(r'\((.+?)\)', source)
    if len(re_year) > 0:
        return re_year[0]
    return ''
def get_douban_url(detail_url):
    """-"""
    detail_soup = get_soup(detail_url).find('a', title='豆瓣链接')
    if detail_soup:
        return detail_soup['href']
    return ''


for itemdoc in ITEMSDOCS:
    item_soup = BeautifulSoup(str(itemdoc), 'html.parser')

    movie_title = item_soup.select_one('.nobr').text
    movie_main_actor = item_soup.select_one('.info > p').text
    movie_douban_rate = item_soup.select_one('.sum').text
    movie_img_url = item_soup.select_one('img')['data-original']
    movie_year = get_year(item_soup.select_one('.thumbnail')['title'])
    movie_pyw_detail = ROOT_URL + item_soup.select_one('.thumbnail')['href']
    movie_douban_url = get_douban_url(movie_pyw_detail)
    print movie_douban_url





