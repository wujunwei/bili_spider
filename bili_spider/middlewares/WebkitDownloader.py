import time
from scrapy.http import HtmlResponse

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class DownloadWebkitMiddleware(object):

    def process_request(self, request, spider):
        driver = webdriver.PhantomJS(desired_capabilities=DesiredCapabilities.PHANTOMJS)
        driver.get(request.url)
        time.sleep(1.3)
        data = driver.page_source
        return HtmlResponse(request.url, body=str(data), encoding='utf-8')

