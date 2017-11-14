# -*- coding: utf-8 -*-

import mysql.connector

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class KeqqPipeline(object):

    def process_item(self, item, spider):
        try:
             conn = mysql.connector.connect(host="127.0.0.1", user="root", password="mysql123", db="keqq")
             cursor = conn.cursor()

             # sql ="insert into course(course_name, sold_count, price, sold_by, link, cid) values('"+item["course_name"][0]+"', '"+item["sold_count"][0]+"', '"+item["price"][0]+"','"+item["sold_by"][0]+"','"+item["link"][0]+"','"+item["cid"][0]+"')";
             sql = "select * from course"             

             # sql = "insert into goods(title, link, price, comment, brand, soldBy) values('"+item["title"][0]+"', '"+item["link"]+"', '"+item["price"][0]+"', '"+item["comment"][0]+"', '"+item['brand'][0]+"', '"+item['soldBy'][0]+"')"
             print(item["course_name"])

             cursor.execute(sql)
             values = cursor.fetchall()
             print(values)
             # cursor.rowcount

             # conn.commit()
             
             cursor.close()
             conn.close()


             return item

        except Exception as e:
            print("You are receiving an error @ # : ", e)
            print("This e.message is very effective: ", e.message)

# https://github.com/scrapy/scrapy/issues/102