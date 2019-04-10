# -*- coding: utf-8 -*-
import scrapy
from collegeSpider.items import CollegespiderItem


class AhjzuSpider(scrapy.Spider):
    name = 'ahjzu'
    allowed_domains = ['ahjzu.edu.cn']
    start_urls = ['http://www.ahjzu.edu.cn/19/list.htm']

    def parse(self, response):
        print(response.request.url)
        # 分组
        li_list = response.xpath("//ul[@class='clearfix']/li")
        for li in li_list:
            item = CollegespiderItem()
            item["title"] = li.xpath("./span[@class='column-news-title']/a/@title").extract_first()
            item["publish_date"] = li.xpath("./span[@class='column-news-date news-date-hide']/text()").extract_first()
            print(item)

        # 翻页
        next_url = response.xpath("//li[@class='page_nav']/a[@class='next']/@href").extract_first()
        if next_url is not None:
            next_url = "http://www.ahjzu.edu.cn/"+next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                dont_filter=True
            )
        # print(next_url)
