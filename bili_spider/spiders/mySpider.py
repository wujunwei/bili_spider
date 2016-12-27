#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
from bili_spider.db import pydb
from bili_spider.user_info import *


class BiliSpider(scrapy.Spider):
    name = "bili"
    allowed_domains = ["bilibili.com"]
    start_urls = [
        "http://space.bilibili.com/1/#!/index"
    ]

    def parse(self, response):
        data = {}
        for key in user_config.keys():
            data[key] = response.xpath(user_config[key]).extract_first()
        data = self.deal_user_info(data)
        pydb.insert_user(data)
        extend_data = {}
        for key in extend_config.keys():
            extend_data[key] = response.xpath(extend_config[key]).extract_first()

            #

    def deal_user_info(self, data):
        for key in data.keys():
            pass
        # todo
        return data
