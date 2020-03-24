# -*- coding: utf-8 -*-

BOT_NAME = 'ebay_crawler'

SPIDER_MODULES = ['ebay_crawler.spiders']
NEWSPIDER_MODULE = 'ebay_crawler.spiders'

# ROBOTSTXT_OBEY = True

# UA 変更
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'

# リクエスト間隔
DOWNLOAD_DELAY = 5

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