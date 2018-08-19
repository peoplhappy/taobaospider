# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
#import fcntl

class TaobaoscrapyPipeline(object):
    def process_item(self, item, spider):
        itemjson = json.dumps(dict(item),ensure_ascii=False)
        #将json写入文件
        f = open("D:/shopinfo.txt", "ab")
        # fcntl.flock(f.fileno(), fcntl.LOCK_EX)  # 加锁
        f.write(itemjson.encode("utf-8"))
        f.close()
        #fcntl.flock(f.fileno(), fcntl.LOCK_UN)  # 解锁
        return item
