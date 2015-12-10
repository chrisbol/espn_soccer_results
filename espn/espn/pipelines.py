# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime

class EspnPipeline(object):
    def process_item(self, item, spider):
        s = int(item['ms'])/1000
        #convert seconds to date
        item['date'] = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
        return item
