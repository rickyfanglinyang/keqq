# -*- coding: utf-8 -*-

import mysql.connector

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class KeqqPipeline(object):

    def process_item(self, item, spider):
        try:
             conn = mysql.connector.connect(host="127.0.0.1", user="root", password="mysql123", db="tb")
             cursor = conn.cursor()

             # sql =""

             # cursor.execute(sql)
             # cursor.rowcount

             # conn.commit()
             
             cursor.close()
             conn.close()


             return item

        except Exception as e:
            print("You are receiving an error @ # : ", e)

