# -*- coding: utf-8 -*-
import scrapy
from  collegeSpider.items import CollegespiderItem

class HfutSpider(scrapy.Spider):
    name = 'hfut'
    allowed_domains = ['hfut.endu.cn']
    start_urls = ['http://news.hfut.edu.cn/list-1-1.html']

    def parse(self, response):
        # 分组
        li_list = response.xpath("//div[@class=' col-lg-8 ']/ul/li[not(@class='bk20 hr')]")
        for li in li_list:
            item = CollegespiderItem()
            item["title"] = li.xpath("./a/@title").extract_first()
            item["publish_date"] = li.xpath("./span/text()").extract_first()
            yield item
            print(item)

        # 翻页
        next_url = "http://news.hfut.edu.cn/"+response.xpath("//div[@class = 'text-c']/a/@href").extract()[-1]
        if next_url != response.request.url:
            # print("ha")
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                dont_filter=True
            )
            # print(response.request.url)
            # print(next_url)


