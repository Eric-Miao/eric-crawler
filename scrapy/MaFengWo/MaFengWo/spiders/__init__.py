# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import re
from scrapy.spiders import Spider
from MaFengWo.items import MafengwoItem

class MafengwoSpider(Spider):
    name = 'douban_movie_top250'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
    
    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url, headers=self.header)
    
    def parse(self, reponse):
        item = MafengwoItem()
        movies = reponse.xpath('//ol[@class="grid_view"]/li')
        for each in movies:
            item['ranking'] = each.xpath(".//div[@class='pic']/em/text()").extract()[0]
            item['name'] = each.xpath(".//div[@class='hd']/a/span[1]/text()").extract()[0]
            item['score'] = each.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['num'] = each.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            item['comment'] = each.xpath('.//p[@class="quote"]/span/text()').extract()[0]
            extra_info = each.xpath(".//div[@class='bd']/p/text()").extract()

            # below is to process the data with regex to get extra information.
            item['director'] = re.findall(r':\s([\w|\s|\S]*)\s{3}', extra_info[0])
            # item['casts'] = extra_info[0].split('主演: ')[1]
            item['year'] = re.findall(r'(\d+)', extra_info[1])
            item['location'] = re.findall(r'/\s([\w\s]*)\s/', extra_info[1])
            item['category'] = re.findall(r'/\s([\w\s]*)\n', extra_info[1])
            yield item

        next_url = reponse.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            print('\n\n\nnext\n\n')
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield scrapy.Request(next_url, headers=self.header)
            
