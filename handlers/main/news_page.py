#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ReS4'

from handlers.base import WebBaseHandler
import json
import urllib

class NewsPageHandler(WebBaseHandler):
    def get(self, _code, *args, **kwargs):

        news = urllib.urlopen("http://www.servicefarsi.com/api/news/3547003931469/7/item={}".format(_code))
        news = news.read()
        news = json.loads(news)

        self.render("page_news.html", news=news['res'])

