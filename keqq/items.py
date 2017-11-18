# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KeqqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    course_name = scrapy.Field()
    sold_count = scrapy.Field()
    price = scrapy.Field()
    sold_by = scrapy.Field()
    link = scrapy.Field()
    cid = scrapy.Field() #course id

class KeqqItemIntro(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    intro_tab = scrapy.Field() # 值：课程概述 
    content_tab = scrapy.Field() # 值：课程目录
    comment_tab = scrapy.Field() # 值：学员评论
    intro_title = scrapy.Field() # 值：简　　介
    intro_detail = scrapy.Field() # 值：简介详情
    teacher_intro_title = scrapy.Field() 
    cid = scrapy.Field() #course id   

class KeqqItemTeacher(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    teacher_id = scrapy.Field()
    teacher_name = scrapy.Field()
    teacher_intro = scrapy.Field()
    cid = scrapy.Field() #course id
    # course_url = scrapy.Field()
    
class KeqqItemTerm(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    term_Name = scrapy.Field()
    term_id = scrapy.Field()
    term_cid = scrapy.Field()
    term_aid = scrapy.Field()

class KeqqItemChapter(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    chapter_term_id = scrapy.Field()
    chapter_aid = scrapy.Field()
    chapter_ch_id = scrapy.Field()
    chapter_cid = scrapy.Field()

class KeqqItemSubInfo(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    sub_info_term_id = scrapy.Field()
    sub_info_csid = scrapy.Field()
    sub_info_cid = scrapy.Field()
    sub_info_sub_id = scrapy.Field()
    sub_info_name = scrapy.Field()  

class KeqqItemTaskInfo(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    task_info_name = scrapy.Field()
    task_info_term_id = scrapy.Field()
    task_info_csid = scrapy.Field()
    task_info_aid = scrapy.Field()
    task_info_cid = scrapy.Field()
    task_info_taid = scrapy.Field()

class KeqqItemComment(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    nick_name = scrapy.Field()
    userid = scrapy.Field()
    first_comment_score = scrapy.Field()
    first_comment_time = scrapy.Field()
    first_comment_progress = scrapy.Field()
    rating = scrapy.Field()
    first_comment = scrapy.Field()
    first_reply = scrapy.Field()
    cid = scrapy.Field()

class KeqqItemList(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    KeqqItem = scrapy.Field()
    KeqqItemTeacher = scrapy.Field()
    KeqqItemTerm = scrapy.Field()
    KeqqItemChapter = scrapy.Field()
    KeqqItemSubInfo = scrapy.Field()
    KeqqItemTaskInfo = scrapy.Field()
    KeqqItemComment = scrapy.Field()
    KeqqItemIntro = scrapy.Field()

