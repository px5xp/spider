# -*- coding: utf-8 -*-
import scrapy
from  collegeSpider.items import CollegespiderItem


class AufeSpider(scrapy.Spider):
    name = 'aufe'
    allowed_domains = ['aufe.edu.cn']
    start_urls = ['http://www.aufe.edu.cn/408/list.htm']

    def parse(self, response):
        print(response.request.url)
        # 分组
        li_list = response.xpath("//div[@class='column-news-list clearfix']/div")
        for li in li_list:
            item = CollegespiderItem()
            item["title"] = li.xpath("./div[@class='news_title']/a/@title").extract_first()
            item["publish_date"] = li.xpath("./div[@class='news_date']/text()").extract_first()
            print(item)

        # 翻页
        next_url = response.xpath("//li[@class='page_nav']/a[@class='next']/@href").extract_first()
        if next_url is not None:
            next_url = "http://www.aufe.edu.cn/"+next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                dont_filter=True
            )
        # print(next_url)
