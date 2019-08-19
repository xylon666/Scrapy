from scrapy import cmdline
cmdline.execute('scrapy crawl douban_spider -o movielist.csv'.split())