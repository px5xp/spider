# -*- coding: utf-8 -*-
import scrapy
from collegeSpider.items import CollegespiderItem

class AhuSpider(scrapy.Spider):
    name = 'ahu'
    allowed_domains = ['ahu.edu.cn']
    start_urls = ['http://news.ahu.edu.cn/4642/list1.htm']

    def parse(self, response):
        print(response.request.url)
        # 分组
        li_list = response.xpath("//ul[@class='wp_article_list']/li")
        for li in li_list:
            item = CollegespiderItem()
            item["title"] = li.xpath("./div[@class='fields pr_fields']/span[@class='Article_Title']/a/@title").extract_first()
            item["publish_date"] = li.xpath("./div[@class='fields ex_fields']/span/text()").extract_first()
            print(item)

        # 翻页
        next_url = response.xpath("//li[@class='page_nav']/a[@class='next']/@href").extract_first()
        if next_url is not None:
            next_url = "http://news.ahu.edu.cn/"+next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                dont_filter=True
            )
        # print(next_url)
