# -*- coding: utf-8 -*-
import scrapy
from scrapyspider.items import ScrapyspiderItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        # print(response.text)
        movies = Selector(response=response).xpath('//div[@class="movie-item film-channel"]')
        num = 0
        for movie in movies:
            link = 'https://maoyan.com' + movie.xpath('./a/@href').extract()[0]
            if num < 10:
                num = num + 1
                yield scrapy.Request(url=link, callback=self.parse2, dont_filter=False)
            else:
                break

    def parse2(self, response):
        # print(response.url)
        movies = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        for movie in movies:
            title = movie.xpath('./h1/text()').extract_first().strip()
            varity = "".join(movie.xpath('//a[@class="text-link"]/text()').extract())
            time = movie.xpath('//li[@class="ellipsis"][last()]/text()').extract_first().strip()

            item = ScrapyspiderItem()
            item['title'] = title
            item['varity'] = varity
            item['time'] = time
            # print(item)
            yield item