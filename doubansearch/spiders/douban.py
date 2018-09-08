# -*- coding: utf-8 -*-
import scrapy
from doubansearch.items import DoubanItem
import re


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list=response.xpath("//div[@class='article']//ol[@class='grid_view']/li ")
        # movie_list=response.css("ol['']")
        for movie in movie_list:
            movie_item=DoubanItem()
            movie_item['serial_number']=movie.xpath(".//div[@class='item']//em/text()").extract_first()

            movie_item['moive_name']=movie.xpath(".//div[@class='item']//span[1]/text()").extract_first()

            content=movie.xpath(".//div[@class='item']//div[@class='bd']/p[1]/text()").extract()

            for item in content:
                content_s=''.join(item.split())
                movie_item['introduce']=content_s

            movie_item['star']=movie.xpath(".//div[@class='info']//div[@class='star']//span[2]/text()").extract_first()

            movie_item['evaluate']=re.search("\d+",movie.xpath(".//div[@class='info']//div[@class='star']//span[4]/text()").extract_first())[0]

            # movie_item['evaluate']=movie.xpath(".//div[@class='info']//div[@class='star']//span[4]/text()").extract_first()
            movie_item['descirbe']=movie.xpath(".//p[@class='quote']/span/text()").extract_first()
            yield  movie_item

        next_page=response.xpath(".//span[@class='next']/link/@href").extract()

        if next_page:
            next_page=next_page[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_page,callback=self.parse)

