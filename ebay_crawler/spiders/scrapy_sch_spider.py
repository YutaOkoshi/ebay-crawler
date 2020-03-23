# -*- coding: utf-8 -*-
import scrapy

from ebay_crawler.items import Post

class ScrapySchSpiderSpider(scrapy.Spider):
    name = 'scrapy_sch_spider'
    allowed_domains = ['www.ebay.com']
    start_urls = [
        'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw=dragonball&LH_PrefLoc=6&rt=nc&LH_Sold=1&LH_Complete=1&_ipg=200'
        ]

    def parse(self, response):
        """
        レスポンスに対するパース処理
        """

        # srp-river-results-listing9 > div > div.s-item__info.clearfix > a
        # /html/body/div[4]/div[5]/div[2]/div[1]/div[2]/ul/li[9]/div/div[2]/a
        for post in response.css('srp-river-results-listing9 > div > div.s-item__info.clearfix > a'):

            print(post)
            yield Post(
                url=post.css('a.s-item__link a::attr(href)').extract_first().strip(),
                title=post.css('a.s-item__link a::text').extract_first().strip(),
                date=post.css('a.s-item__link span.date a::text').extract_first().strip(),
            )
