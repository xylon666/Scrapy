# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanItem
import codecs

with codecs.open('movielist.csv','wb+') as f:
    f.write(codecs.BOM_UTF8)

class DoubanSpiderSpider(scrapy.Spider):
    #爬虫名称
    name = 'douban_spider'
    #爬虫允许抓取的域名
    allowed_domains = ['movie.douban.com']
    #获取数据传给调度器的地址
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for item in movie_list:
            douban_item = DoubanItem()
            douban_item['movie_num'] = item.xpath(".//div[@class='item']//em/text()").get()
            douban_item['movie_name'] = item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").get()
            douban_item['star'] = item.xpath(".//div[@class='bd']/div[@class='star']/span[2]/text()").get()
            douban_item['value'] = item.xpath(".//div[@class='bd']/div[@class='star']/span[4]/text()").get()
            douban_item['describle'] = item.xpath(".//div[@class='bd']/p[@class='quote']/span/text()").get()
            print(douban_item)
            yield douban_item
            #将返回结果压入item Pipline进行处理
        next_link = response.xpath("//span[@class='next']/link/@href").get()
        if next_link:
            print('-------------' + str(next_link))
            yield scrapy.Request('http://movie.douban.com/top250' + next_link, callback=self.parse)