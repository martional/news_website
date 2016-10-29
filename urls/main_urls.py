#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.main import home_news, news_page

__author__ = 'ReS4'

url_patterns = [
    ("/", home_news.HomeNewsHandler, None, "home"),

    ("/news_page/([\w+]+)", news_page.NewsPageHandler),
    ("/news_page/([\w+]-(\d+))", news_page.NewsPageHandler, None, "a:news_page"),
]

