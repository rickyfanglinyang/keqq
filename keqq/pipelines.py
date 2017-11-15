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
             logging.info("This is an info @ process_item()")

             if "KeqqItem" in item:
                print("@ KeqqItem")
                logging.info("This is an info @ KeqqItem")
                print("in course_name")
                for i in range(len(item["KeqqItem"])):
                    sql ="insert into course(course_name, sold_count, price, sold_by, link, cid) \
                    values('"+item["KeqqItem"][i]["course_name"]+"', '"+item["KeqqItem"][i]["sold_count"]+"', '"+item["KeqqItem"][i]["price"]+"','"+item["KeqqItem"][i]["sold_by"]+"','"+item["KeqqItem"][i]["link"]+"','"+item["KeqqItem"][i]["cid"]+"')";
                    logging.info("sql %s @ KeqqItem" %sql)
                    logging.info("Before executing ### : sql %s @ KeqqItemComment" %sql)
                    self.cursor.execute(sql)
                    logging.info("After self.cursor.execute(sql) executing ### : sql %s @ KeqqItemComment" %sql)
                    self.conn.commit()

             if "KeqqItemIntro" in item:
                print("in intro_detail @@@@:", str(item["KeqqItemIntro"][i]["cid"]))
                for i in range(len(item["KeqqItemIntro"])):
                    sql ="insert into courseIntro(intro_tab, content_tab, comment_tab, intro_title, intro_detail, teacher_intro_title, cid) \
                    values('"+str(item["KeqqItemIntro"][i]["intro_tab"])+"', '"+str(item["KeqqItemIntro"][i]["content_tab"])+"', '"+str(item["KeqqItemIntro"][i]["comment_tab"]) \
                    +"','"+str(item["KeqqItemIntro"][i]["intro_title"])+"','"+str(item["KeqqItemIntro"][i]["intro_detail"])+"','"+str(item["KeqqItemIntro"][i]["teacher_intro_title"]) \
                    +"','"+str(item["KeqqItemIntro"][i]["cid"])+"')";
                    logging.info("sql %s @ KeqqItemIntro" %sql)
                    logging.info("Before executing ### : sql %s @ KeqqItemComment" %sql)
                    self.cursor.execute(sql)
                    logging.info("After self.cursor.execute(sql) executing ### : sql %s @ KeqqItemComment" %sql)
                    self.conn.commit()

             if "KeqqItemTeacher" in item:
                for i in range(len(item["KeqqItemTeacher"])):
                    print("in teacher_name")
                    sql ="insert into teacher(teacher_id, teacher_name, teacher_intro, cid) \
                    values('"+item["KeqqItemTeacher"][i]["teacher_id"]+"', '"+item["KeqqItemTeacher"][i]["teacher_name"]+"', '"+item["KeqqItemTeacher"][i]["teacher_intro"]+"','"+item["KeqqItemTeacher"][i]["cid"]+"')";
                    logging.info("sql %s @ KeqqItem" %sql)
                    logging.info("Before executing ### : sql %s @ KeqqItemComment" %sql)
                    self.cursor.execute(sql)
                    logging.info("After self.cursor.execute(sql) executing ### : sql %s @ KeqqItemComment" %sql)
                    self.conn.commit()

             if "KeqqItemTerm" in item:
                print("in term_Name")
                for i in range(len(item["KeqqItemTeacher"])):
                    sql ="insert into term(term_Name, term_id, term_cid, term_aid) \
                    values('"+item["KeqqItemTerm"][i]["term_Name"]+"', '"+str(item["KeqqItemTerm"][i]["term_id"])+"', '"+str(item["KeqqItemTerm"][i]["term_cid"])+"','"+str(item["KeqqItemTerm"][i]["term_aid"])+"')";
                    logging.info("Before executing ### : sql %s @ KeqqItemComment" %sql)
                    self.cursor.execute(sql)
                    logging.info("After self.cursor.execute(sql) executing ### : sql %s @ KeqqItemComment" %sql)
                    self.conn.commit()
             if "KeqqItemChapter" in item:
                print("in chapter_term_id")
                for i in range(len(item["KeqqItemChapter"])):
                    sql ="insert into Chapter(chapter_term_id, chapter_aid, chapter_ch_id, chapter_cid) \
                    values('"+str(item["KeqqItemChapter"][i]["chapter_term_id"])+"', '"+str(item["KeqqItemChapter"][i]["chapter_aid"])+"', '"+str(item["KeqqItemChapter"][i]["chapter_ch_id"])+"','"+str(item["KeqqItemChapter"][i]["chapter_cid"])+"')";
                    logging.info("Before executing ### : sql %s @ KeqqItemComment" %sql)
                    self.cursor.execute(sql)
                    logging.info("After self.cursor.execute(sql) executing ### : sql %s @ KeqqItemComment" %sql)
                    self.conn.commit()
                logging.info("sql %s @ KeqqItem" %sql)
             if "KeqqItemSubInfo" in item:
                print("in sub_info_term_id")
                for i in range(len(item["KeqqItemSubInfo"])):
                    sql ="insert into SubInfo(sub_info_term_id, sub_info_csid, sub_info_cid, sub_info_sub_id, sub_info_name) \
                    values('"+str(item["KeqqItemSubInfo"][i]["sub_info_term_id"])+"', '"+str(item["KeqqItemSubInfo"][i]["sub_info_csid"])+"', '"+str(item["KeqqItemSubInfo"][i]["sub_info_cid"])+"','"+str(item["KeqqItemSubInfo"][i]["sub_info_sub_id"])+"','"+str(item["KeqqItemSubInfo"][i]["sub_info_name"])+"')";
                    logging.info("Before executing ### : sql %s @ KeqqItemComment" %sql)
                    self.cursor.execute(sql)
                    logging.info("After self.cursor.execute(sql) executing ### : sql %s @ KeqqItemComment" %sql)
                    self.conn.commit()
                logging.info("sql %s @ KeqqItem" %sql)
             if "KeqqItemTaskInfo" in item:
                for i in range(len(item["KeqqItemTaskInfo"])):
                    print("in task_info_name")
                    sql ="insert into TaskInfo(task_info_name, task_info_term_id, task_info_csid, task_info_aid, task_info_cid, task_info_taid) \
                    values('"+item["KeqqItemTaskInfo"][i]["task_info_name"]+"', '"+str(item["KeqqItemTaskInfo"][i]["task_info_term_id"])+"', '"+str(item["KeqqItemTaskInfo"][i]["task_info_csid"])+"','"+str(item["KeqqItemTaskInfo"][i]["task_info_aid"])+"','"+str(item["KeqqItemTaskInfo"][i]["task_info_cid"])+"','"+str(item["KeqqItemTaskInfo"][i]["task_info_taid"])+"')";
                    logging.info("Before executing ### : sql %s @ KeqqItemComment" %sql)
                    self.cursor.execute(sql)
                    logging.info("After self.cursor.execute(sql) executing ### : sql %s @ KeqqItemComment" %sql)
                    self.conn.commit()
                logging.info("sql %s @ KeqqItem" %sql)
             if "KeqqItemComment" in item:
                print("in first_comment")
                for i in range(len(item["KeqqItemComment"])):
                    sql ="insert into comment(nick_name, userid, first_comment_score, first_comment_time, first_comment_progress, rating, first_comment, cid) \
                    values('"+item["KeqqItemComment"][i]["nick_name"]+"', '"+str(item["KeqqItemComment"][i]["userid"])+"', '"+str(item["KeqqItemComment"][i]["first_comment_score"])+"','"+str(item["KeqqItemComment"][i]["first_comment_time"]) \
                    +"','"+str(item["KeqqItemComment"][i]["first_comment_progress"])+"','"+str(item["KeqqItemComment"][i]["rating"])+"','"+item["KeqqItemComment"][i]["first_comment"]+"','"+str(item["KeqqItemComment"][i]["cid"])+"')";
                    logging.info("Before executing ### : sql %s @ KeqqItemComment" %sql)
                    self.cursor.execute(sql)
                    logging.info("After self.cursor.execute(sql) executing ### : sql %s @ KeqqItemComment" %sql)
                    self.conn.commit()
                logging.info("sql %s @ KeqqItemComment" %sql)

             print("End of process_item!!!####")
             print("@@item@@", item)

             return item

        except Exception as e:
            print("You are receiving an error @ # : %s" %e)
            print("This e.message is very effective: ", e.message)

# https://github.com/scrapy/scrapy/issues/1i2
# https://stackoverflow.com/questions/18364333/scrapy-suggestion-for-multiple-returns-items-to-database