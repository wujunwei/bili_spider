#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy
import bili_spider.db.pydb


class BiliSpider(scrapy.Spider):
    name = "bili"
    allowed_domains = ["bilibili.com"]
    start_urls = [
        r"http://space.bilibili.com/2994719/#!/index"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)