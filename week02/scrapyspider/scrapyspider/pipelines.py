# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pq 

class ScrapyspiderPipeline:
    # initialize mysql connection and cursor
    def __init__(self):
        self.conn = pq.connect(host='localhost', user='guokai',
                               passwd='guokaiwhu', db='test', charset='utf8mb4')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            title = item['title']
            varity = item['varity']
            time = item['time']

            # execute insert sql
            sql = '''insert into maoyanmovie(title,varity,time) values (%s, %s, %s)'''
            self.cur.execute(sql, (title, varity, time))
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            pass
        
    # close cursor and connection
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()