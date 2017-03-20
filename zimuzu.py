#!/usr/bin/python
# -*- coding: UTF-8 -*-
from utils.model import Film
from utils.getSoup import getSoup

rootUrl = "http://www.zimuzu.tv/"

soup = getSoup(rootUrl)
print soup


