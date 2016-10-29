#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'ReS4'

from handlers.base import WebBaseHandler
import json
import urllib


class HomeNewsHandler(WebBaseHandler):
    def get(self, *args, **kwargs):
        states = urllib.urlopen("http://www.servicefarsi.com/api/news/3547003931469/2/")
        states = states.read()
        states = json.loads(states)

        categoris = urllib.urlopen("http://www.servicefarsi.com/api/news/3547003931469/1/")
        categoris = categoris.read()
        categoris = json.loads(categoris)

        state_news = urllib.urlopen("http://www.servicefarsi.com/api/news/3547003931469/4/item=17,page=1")
        state_news = state_news.read()
        state_news = json.loads(state_news)

        news_cat = urllib.urlopen("http://www.servicefarsi.com/api/news/3547003931469/4/item=1,page=1")
        news_cat = news_cat.read()
        news_cat = json.loads(news_cat)

        self.render("home_news.html", states=states['res'], categoris=categoris['res'], state_news=state_news['res'],
                    news_cat=news_cat['res'])

    def post(self, *args, **kwargs):
        newsid = self.get_argument("id", None)
        url = "http://www.servicefarsi.com/api/news/3547003931469/4/item=" + newsid + ",page=1"
        news = urllib.urlopen(url)
        news = news.read()
        news = json.loads(news)
        self.write({"data": news})
