# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ShanghaiTechProf

class ShanghaitechSpider(scrapy.Spider):
    name = 'shanghaitech'
    # allowed_domains = ['www.shanghaitech.edu.cn']
    start_urls = ['http://hr.shanghaitech.edu.cn/xxkxyjsxy/list1.htm']

      
    def parse(self, response):
        
        prof = ShanghaiTechProf()

        for each in response.xpath("//li[contains(@class,'news_admin')]"):
            name = each.xpath("./div[@class='content']/p[@class='bt']/a/@title").extract()
            title = each.xpath("./div[@class='content']/p[@class='job']/text()").extract()
            direction = each.xpath("./div[@class='content']/p[@class='lab']/text()").extract()
            prof['name'] = name[0]
            prof['title'] = title[0]
            prof['direction'] = direction[0]

            yield prof
            
        next_url = response.xpath('//a[@class="next"]/@href').extract()

        if next_url:
            next_url = 'http://hr.shanghaitech.edu.cn' + next_url[0]
            # next_url = response.urljoin(next_url[0])
            yield scrapy.Request(next_url)