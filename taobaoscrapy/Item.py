# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# to collect taobaos sell data
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#抽取内容店名称，一个月的销售数量，总销售量，评价数据，商品名称，店铺url,价格变化
class taobaoscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    shopname=scrapy.Field()
    lastmonthsells=scrapy.Field()
    totalsells=scrapy.Field()
    rated=scrapy.Field()
    goodsname=scrapy.Field()
    shopurl=scrapy.Field()
    pricelist=scrapy.Field()
    pass
