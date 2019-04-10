# -*- coding: utf-8 -*-
import scrapy
from  collegeSpider.items import CollegespiderItem



class UstcSpider(scrapy.Spider):
    name = 'ustc'
    allowed_domains = ['news.ustc.edu.cn']
    start_urls = ['http://news.ustc.edu.cn/xwbl/list.htm']

    def parse(self, response):
        # 分组
        li_list = response.xpath("//div[@id='wp_news_w3']/li")
        for li in li_list:
            item = CollegespiderItem()
            item["title"] = li.xpath("./a/@title").extract_first()
            item["publish_date"] = li.xpath("./span/text()").extract_first()
            yield item
            print(item)

        # 翻页
        next_url = response.xpath("//li[@class='page_nav']/a[@class='next']/@href").extract_first()
        print(next_url)
        # if next_url is not None:
        #     next_url = "http://news.hfut.edu.cn/"+next_url
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse,
        #         dont_filter=True
        #     )
