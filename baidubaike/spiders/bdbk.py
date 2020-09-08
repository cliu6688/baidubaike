# -*- coding: utf-8 -*-
import scrapy


class BdbkSpider(scrapy.Spider):
    name = 'bdbk'
    allowed_domains = ['https://baike.baidu.com/']
    start_urls = ['https://baike.baidu.com/']

    def parse(self, response):
        list_selector = response.xpath('/html//text()')
        # list_selector = response.xpath('//span[@class="ref"]//text()')
        for one_selector in list_selector:
            print (one_selector)
        # print (response.text())
        # pass
