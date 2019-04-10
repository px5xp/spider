# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook

class CollegespiderPipeline(object):
    # def __init__(self):
    #     self.wb = Workbook()
    #     self.ws = self.wb.active
    #     self.ws.append(['title', 'publish_date'])
    def process_item(self, item, spider):
        # line = [item["title"], item["publish_date"]]
        # self.ws.append(line)
        # self.wb.save("hfut.csv")
        return item

