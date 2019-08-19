# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 排名
    movie_num = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 星级
    star = scrapy.Field()
    # 评价人数
    value = scrapy.Field()
    # 描述
    describle = scrapy.Field()