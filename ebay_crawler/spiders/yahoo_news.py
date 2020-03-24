# -*- coding: utf-8 -*-
import scrapy


class YahooNewsSpider(scrapy.Spider):
    name = 'yahoo_news'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/']

    def parse(self, response):
        print('ニュースリンク一覧:')
        print(response.css('.topicsListItem a::attr("href")').extract())
        pass
