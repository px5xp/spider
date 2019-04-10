# -*- coding: utf-8 -*-
import scrapy
from  collegeSpider.items import CollegespiderItem

class AustSpider(scrapy.Spider):
    name = 'aust'
    allowed_domains = ['aust.edu.cn']
    start_urls = ['http://news.aust.edu.cn/xxxw.htm']

    def parse(self, response):
        # 分组
        li_list = response.xpath("//div[@class='list-r-c']/ul/li")
        # print(li_list)
        for li in li_list:
            item = CollegespiderItem()
            item["title"] = li.xpath("./a/@title").extract_first()
            item["publish_date"] = li.xpath("./font/text()").extract_first()
            yield item
            print(item)
        # 翻页
        next_url = response.xpath("//a[text()='下页']/@href").extract_first()
        if next_url is not None:
            if "xxxw" in next_url:
                next_url = "http://news.aust.edu.cn/" + next_url
            else:
                next_url = "http://news.aust.edu.cn/xxxw/" + next_url

            yield scrapy.Request(
                next_url,
                callback=self.parse,
                dont_filter=True
            )
        print(next_url)

