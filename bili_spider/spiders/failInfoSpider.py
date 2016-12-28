#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

import scrapy
from bili_spider.db import pydb
from bili_spider.user_info import *


class BiliSpider(scrapy.Spider):
    name = "failed"
    allowed_domains = ["bilibili.com"]
    start_urls = [

    ]
    last_id = 2000
    url = ("http://space.bilibili.com/", "/#!/index")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        info_arr = pydb.get_fail_user(self.last_id)
        for i in info_arr:
            self.start_urls.append(self.url[0] + str(i[0]) + self.url[1])
        # print(self.start_urls)

    def parse(self, response):
        user_id = re.match("^http://space.bilibili.com/(\d+)/", response.url).group(1)
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
            pydb.update_user(user_id, data)
            pydb.update_extend_user(user_id, extend_data)
        except Exception as e:
            print(e)
            exit()

    def __del__(self):
        pydb.close()
