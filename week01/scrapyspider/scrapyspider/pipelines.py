# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyspiderPipeline:
    def process_item(self, item, spider):
        title = item['title']
        varity = item['varity']
        time = item['time']
        output = f'|{title}|\t|{varity}|\t|{time}|\n\n'
        # print(output)
        with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
