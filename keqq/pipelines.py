# -*- coding: utf-8 -*-

import mysql.connector
import logging

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class KeqqPipeline(object):

    def __init__(self):
        self.conn = mysql.connector.connect(host="127.0.0.1", user="root", password="mysql123", db="keqq")
        self.cursor = self.conn.cursor(buffered=True,dictionary=True)
        print("@ __init__ of KeqqPipeline")
        logging.info("This is an info @ __init__ of KeqqPipeline")

    def process_item(self, item, spider):
        try:
             # conn = mysql.connector.connect(host="127.0.0.1", user="root", password="mysql123", db="keqq")
             # cursor = conn.cursor()

             # sql ="insert into course(course_name, sold_count, price, sold_by, link, cid) values('"+item["course_name"]+"', '"+item["sold_count"]+"', '"+item["price"]+"','"+item["sold_by"]+"','"+item["link"]+"','"+item["cid"]+"')";
                      

             # sql = "insert into goods(title, link, price, comment, brand, soldBy) values('"+item["title"]+"', '"+item["link"]+"', '"+item["price"]+"', '"+item["comment"]+"', '"+item['brand']+"', '"+item['soldBy']+"')"
             # print(item["course_name"])

             # self.cursor.execute(sql)
             # values = self.cursor.fetchall()
             # print("values @####: ", values)
             # cursor.rowcount

             logging.info("This is an info @ process_item()")

             # if 'KeqqItem' in item:
             #    print("@ KeqqItem")
             #    logging.info("This is an info @ KeqqItem")
             #    print("in course_name")
             #    sql ="insert into course(course_name, sold_count, price, sold_by, link, cid) \
             #    values('"+item["KeqqItem"]["course_name"]+"', '"+item["KeqqItem"]["sold_count"]+"', '"+item["KeqqItem"]["price"]+"','"+item["KeqqItem"]["sold_by"]+"','"+item["KeqqItem"]["link"]+"','"+item["KeqqItem"]["cid"]+"')";
             #    logging.info("sql %s @ KeqqItem" %sql)
             #    # self.cursor.execute(sql)
             # elif 'KeqqItemChapter' in item:
             #    print("@ KeqqItemTeacher")
             # elif 'KeqqItemTerm' in item:
             #    print("@ KeqqItemTerm")
             # elif 'KeqqItemChapter' in item:
             #    print("@ KeqqItemChapter")
             # elif 'KeqqItemSubInfo' in item:
             #    print("@ KeqqItemSubInfo")
             # elif 'KeqqItemTaskInfo' in item:
             #    print("@ KeqqItemTaskInfo")
             # elif 'KeqqItemComment' in item:
             #    print("@ KeqqItemComment")
             # elif 'KeqqItemIntro' in item:
             #    print("@ KeqqItemIntro")
             # else:
             #    print("@ else ")


             if "KeqqItem" in item:
                print("@ KeqqItem")
                logging.info("This is an info @ KeqqItem")
                print("in course_name")
                sql ="insert into course(course_name, sold_count, price, sold_by, link, cid) \
                values('"+item["KeqqItem"][0]["course_name"]+"', '"+item["KeqqItem"][0]["sold_count"]+"', '"+item["KeqqItem"][0]["price"]+"','"+item["KeqqItem"][0]["sold_by"]+"','"+item["KeqqItem"][0]["link"]+"','"+item["KeqqItem"][0]["cid"]+"')";
                logging.info("sql %s @ KeqqItem" %sql)
             if "KeqqItemIntro" in item:
                print("in intro_detail @@@@:", str(item["KeqqItemIntro"]["cid"]))

                sql ="insert into courseIntro(intro_tab, content_tab, comment_tab, intro_title, intro_detail, teacher_intro_title, cid) \
                values('"+str(item["KeqqItemIntro"]["intro_tab"])+"', '"+str(item["KeqqItemIntro"]["content_tab"])+"', '"+str(item["KeqqItemIntro"]["comment_tab"]) \
                +"','"+str(item["KeqqItemIntro"]["intro_title"])+"','"+str(item["KeqqItemIntro"]["intro_detail"])+"','"+str(item["KeqqItemIntro"]["teacher_intro_title"]) \
                +"','"+str(item["KeqqItemIntro"]["cid"])+"')";


                logging.info("sql %s @ KeqqItemIntro" %sql)
             if "KeqqItemTeacher" in item:
                print("in teacher_name")
                sql ="insert into teacher(teacher_id, teacher_name, teacher_intro, cid) \
                values('"+item["KeqqItemTeacher"][0]["teacher_id"]+"', '"+item["KeqqItemTeacher"][0]["teacher_name"]+"', '"+item["KeqqItemTeacher"][0]["teacher_intro"]+"','"+item["KeqqItemTeacher"][0]["cid"]+"')";
                logging.info("sql %s @ KeqqItem" %sql)
             if "KeqqItemTerm" in item:
                print("in term_Name")
                sql ="insert into term(term_Name, term_id, term_cid, term_aid) \
                values('"+item["KeqqItemTerm"][0]["term_Name"]+"', '"+str(item["KeqqItemTerm"][0]["term_id"])+"', '"+str(item["KeqqItemTerm"][0]["term_cid"])+"','"+str(item["KeqqItemTerm"][0]["term_aid"])+"')";
                logging.info("sql %s @ KeqqItem" %sql)
             if "KeqqItemChapter" in item:
                print("in chapter_term_id")
                sql ="insert into Chapter(chapter_term_id, chapter_aid, chapter_ch_id, chapter_cid) \
                values('"+str(item["KeqqItemChapter"][0]["chapter_term_id"])+"', '"+str(item["KeqqItemChapter"][0]["chapter_aid"])+"', '"+str(item["KeqqItemChapter"][0]["chapter_ch_id"])+"','"+str(item["KeqqItemChapter"][0]["chapter_cid"])+"')";
                logging.info("sql %s @ KeqqItem" %sql)
             if "KeqqItemSubInfo" in item:
                print("in sub_info_term_id")
                sql ="insert into SubInfo(sub_info_term_id, sub_info_csid, sub_info_cid, sub_info_sub_id, sub_info_name) \
                values('"+str(item["KeqqItemSubInfo"][0]["sub_info_term_id"])+"', '"+str(item["KeqqItemSubInfo"][0]["sub_info_csid"])+"', '"+str(item["KeqqItemSubInfo"][0]["sub_info_cid"])+"','"+str(item["KeqqItemSubInfo"][0]["sub_info_sub_id"])+"','"+str(item["KeqqItemSubInfo"][0]["sub_info_name"])+"')";
                logging.info("sql %s @ KeqqItem" %sql)
             if "KeqqItemTaskInfo" in item:
                print("in task_info_name")
                sql ="insert into TaskInfo(task_info_name, task_info_term_id, task_info_csid, task_info_aid, task_info_cid, task_info_taid) \
                values('"+item["KeqqItemTaskInfo"][0]["task_info_name"]+"', '"+str(item["KeqqItemTaskInfo"][0]["task_info_term_id"])+"', '"+str(item["KeqqItemTaskInfo"][0]["task_info_csid"])+"','"+str(item["KeqqItemTaskInfo"][0]["task_info_aid"])+"','"+str(item["KeqqItemTaskInfo"][0]["task_info_cid"])+"','"+str(item["KeqqItemTaskInfo"][0]["task_info_taid"])+"')";
                logging.info("sql %s @ KeqqItem" %sql)
             if "KeqqItemComment" in item:
                print("in first_comment")
                sql ="insert into comment(nick_name, userid, first_comment_score, first_comment_time, first_comment_progress, rating, first_comment, cid) \
                values('"+item["KeqqItemComment"][0]["nick_name"]+"', '"+str(item["KeqqItemComment"][0]["userid"])+"', '"+str(item["KeqqItemComment"][0]["first_comment_score"])+"','"+str(item["KeqqItemComment"][0]["first_comment_time"]) \
                +"','"+str(item["KeqqItemComment"][0]["first_comment_progress"])+"','"+item["KeqqItemComment"][0]["first_comment"]+"','"+str(item["KeqqItemComment"][0]["cid"])+"')";
                logging.info("sql %s @ KeqqItemComment" %sql)
             # else:
             #    print("in else")
             #    sql = "select * from course"    
             #    # self.cursor.execute(sql)
             #    # values = self.cursor.fetchall()
             #    print("values @####: ", values)
             # if sql:
             #    print("Empty sql@#$")
             #    return

             self.cursor.execute(sql)
             self.conn.commit()
             
             # cursor.close()
             # conn.close()

             print("End of process_item!!!####")
             print("@@item@@", item)

             return item

        except Exception as e:
            print("You are receiving an error @ # : %s" %e)
            print("This e.message is very effective: ", e.message)

# https://github.com/scrapy/scrapy/issues/102
# https://stackoverflow.com/questions/18364333/scrapy-suggestion-for-multiple-returns-items-to-database