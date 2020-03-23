# -*- coding: utf-8 -*-

BOT_NAME = 'ebay_crawler'

SPIDER_MODULES = ['ebay_crawler.spiders']
NEWSPIDER_MODULE = 'ebay_crawler.spiders'

ROBOTSTXT_OBEY = True

# リクエスト間隔
DOWNLOAD_DELAY = 3

# キャッシュ有効か
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#日本語文字化けのためにEncode設定
FEED_EXPORT_ENCODING='utf-8'
# 出力形式
FEED_FORMAT = 'csv'