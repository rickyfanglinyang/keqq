# -*- coding: utf-8 -*-

import mysql.connector

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class KeqqPipeline(object):

    def __init__(self):
        self.conn = mysql.connector.connect(host="127.0.0.1", user="root", password="mysql123", db="keqq")
        self.cursor = self.conn.cursor(buffered=True,dictionary=True)

    def process_item(self, item, spider):
        try:
             # conn = mysql.connector.connect(host="127.0.0.1", user="root", password="mysql123", db="keqq")
             # cursor = conn.cursor()

             # sql ="insert into course(course_name, sold_count, price, sold_by, link, cid) values('"+item["course_name"][0]+"', '"+item["sold_count"][0]+"', '"+item["price"][0]+"','"+item["sold_by"][0]+"','"+item["link"][0]+"','"+item["cid"][0]+"')";
             sql = "select * from course"             

             # sql = "insert into goods(title, link, price, comment, brand, soldBy) values('"+item["title"][0]+"', '"+item["link"]+"', '"+item["price"][0]+"', '"+item["comment"][0]+"', '"+item['brand'][0]+"', '"+item['soldBy'][0]+"')"
             # print(item["course_name"])

             # self.cursor.execute(sql)
             # values = self.cursor.fetchall()
             # print("values @####: ", values)
             # cursor.rowcount

             if 'KeqqItem' in item:
                print("@ KeqqItem")
             elif 'KeqqItemTeacher' in item:
                print("@ KeqqItemTeacher")
             elif 'KeqqItemTerm' in item:
                print("@ KeqqItemTerm")
             elif 'KeqqItemChapter' in item:
                print("@ KeqqItemChapter")
             elif 'KeqqItemSubInfo' in item:
                print("@ KeqqItemSubInfo")
             elif 'KeqqItemTaskInfo' in item:
                print("@ KeqqItemTaskInfo")
             elif 'KeqqItemComment' in item:
                print("@ KeqqItemComment")
             elif 'KeqqItemIntro' in item:
                print("@ KeqqItemIntro")
             else:
                print("@ else ")


             if "course_name" in item:
                print("in course_name")
                sql ="insert into course(course_name, sold_count, price, sold_by, link, cid) \
                values('"+item["course_name"][0]+"', '"+item["sold_count"][0]+"', '"+item["price"][0]+"','"+item["sold_by"][0]+"','"+item["link"][0]+"','"+item["cid"][0]+"')";
                # self.cursor.execute(sql)
             elif "intro_detail" in item:
                print("in intro_detail")
                sql ="insert into courseIntro(intro_tab, content_tab, comment_tab, intro_title, intro_detail, teacher_intro_title, cid) \
                values('"+item["intro_tab"][0]+"', '"+item["content_tab"][0]+"', '"+item["comment_tab"][0]+"','"+item["intro_title"][0]+"','"+item["intro_detail"][0]+"','"+item["teacher_intro_title"][0]+"','"+item["cid"][0]+"')";
             elif "teacher_name" in item:
                print("in teacher_name")
                sql ="insert into teacher(teacher_id, teacher_name, teacher_intro, cid) \
                values('"+item["teacher_id"][0]+"', '"+item["teacher_name"][0]+"', '"+item["teacher_intro"][0]+"','"+item["cid"][0]+"')";
             elif "term_Name" in item:
                print("in term_Name")
                sql ="insert into term(term_Name, term_id, term_cid, term_aid) \
                values('"+item["term_Name"][0]+"', '"+item["term_id"][0]+"', '"+item["term_cid"][0]+"','"+item["term_aid"][0]+"')";
             elif "chapter_term_id" in item:
                print("in chapter_term_id")
                sql ="insert into Chapter(chapter_term_id, chapter_aid, chapter_ch_id, chapter_cid) \
                values('"+item["chapter_term_id"][0]+"', '"+item["chapter_aid"][0]+"', '"+item["chapter_ch_id"][0]+"','"+item["chapter_cid"][0]+"')";
             elif "sub_info_term_id" in item:
                print("in sub_info_term_id")
                sql ="insert into SubInfo(sub_info_term_id, sub_info_csid, sub_info_cid, sub_info_sub_id, sub_info_name) \
                values('"+item["sub_info_term_id"][0]+"', '"+item["sub_info_csid"][0]+"', '"+item["sub_info_cid"][0]+"','"+item["sub_info_sub_id"][0]+"','"+item["sub_info_name"][0]+"')";
             elif "task_info_name" in item:
                print("in task_info_name")
                sql ="insert into TaskInfo(task_info_name, task_info_term_id, task_info_csid, task_info_aid, task_info_cid, task_info_taid) \
                values('"+item["task_info_name"][0]+"', '"+item["task_info_term_id"][0]+"', '"+item["task_info_csid"][0]+"','"+item["task_info_aid"][0]+"','"+item["task_info_cid"][0]+"','"+item["task_info_taid"][0]+"')";
             elif "first_comment" in item:
                print("in first_comment")
                sql ="insert into comment(nick_name, userid, first_comment_score, first_comment_time, first_comment_progress, rating, first_comment, cid) \
                values('"+item["nick_name"][0]+"', '"+item["userid"][0]+"', '"+item["first_comment_score"][0]+"','"+item["first_comment_time"][0]+"','"+item["first_comment_progress"][0]+"','"+item["first_comment"][0]+"','"+item["cid"][0]+"')";
             else:
                print("in else")
                self.cursor.execute(sql)
                values = self.cursor.fetchall()
                print("values @####: ", values)

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