#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
from bili_spider.db import pydb
from bili_spider.user_info import *


class BiliSpider(scrapy.Spider):
    name = "bili"
    allowed_domains = ["bilibili.com"]
    start_urls = [

    ]
    url = ("http://space.bilibili.com/", "/#!/index")
    start = 3101
    step = 100

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(self.start, self.start + self.step):
            self.start_urls.append(self.url[0] + str(i) + self.url[1])
        # print(self.start_urls)

    def parse(self, response):
        data = {}
        extend_data = {}
        if response.status == 200:
            for key in user_config.keys():
                data[key] = response.xpath(user_config[key]).extract_first()
            data = deal_user_info(data)
            for key in extend_config.keys():
                extend_data[key] = response.xpath(extend_config[key]).extract_first()
            extend_data = deal_user_info(extend_data)
        try:
            user_id = pydb.insert_user(data)
            pydb.insert_extend_user(user_id, extend_data)
        except Exception as e:
            print(e)
            exit()

    def __del__(self):
        pydb.close()
