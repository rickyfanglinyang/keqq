# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.http import Request
from keqq.items import KeqqItem
from keqq.items import KeqqItemIntro
from keqq.items import KeqqItemTeacher
from keqq.items import KeqqItemTerm 
from keqq.items import KeqqItemChapter
from keqq.items import KeqqItemSubInfo 
from keqq.items import KeqqItemTaskInfo 
from keqq.items import KeqqItemComment
from keqq.items import KeqqItemList
# import keqq.items # doesn't work
import json
import os
import re

class KeSpider(scrapy.Spider):
    name = 'ke'
    allowed_domains = ['ke.qq.com']
    start_urls = ['http://ke.qq.com/']
    downlaod_deplay = 10
   

    # print("starting to launch request..... in %s"%start_urls)
    logging.basicConfig(filename="F:/appDataPractice/scrapy/keqq/logmeDebug.txt", level=logging.DEBUG)

    def parse(self, response):
        # item = KeqqItemList()
        # print("This is the start of response --------------------------")
        # result = response.body.decode('utf-8', 'ignore')
        # pagetitle = response.xpath("//title/text()").extract()
        # print(pagetitle)

        # title = "title: " + str(pagetitle)
        # savefield(title, "del")
        # savefield(title)       


        key = "宝医堂中医" # "音乐窝" # "腾讯课堂设计大师班"  #"顾忠的贝斯世界俱乐部" # "While老师主讲-高薪就业python自动化运维云计算企业实战课程" 
        for i in range(1,2):
            url = "https://ke.qq.com/course/list/"+str(key)+"?page="+str(i)
            logging.debug(" [壹]This is a debug message @#: " + url)

            yield Request(url=url, callback=self.page)

        # logging.debug("This is a debug message @ end of parse(self, response)")    

    def page(self, response):
       
        logging.debug(" [贰]This is a debug message @ page(self, response)")    
        for course in response.xpath("//div[@class='main-left']/div[@class='market-bd market-bd-6 course-list course-card-list-multi-wrap']/ul[@class='course-card-list']/li[@class='course-card-item']"):
            course_name = course.xpath("./h4[@class='item-tt']/a[@class='item-tt-link']/text()").extract_first()
            sold_count  = course.xpath("./div[@class='item-line item-line--middle']/span[@class='line-cell item-user']/text()").extract_first()
            price  = course.xpath("./div[@class='item-line item-line--bottom']/span[@class='line-cell item-price']/text()").extract_first()
            sold_by  = course.xpath("./div[@class='item-line item-line--middle']/span[@class='item-source']/a[@class='item-source-link']/text()").extract_first()
            link = "https:" + str(course.xpath("./a/@href").extract_first()).strip() # Remove space in front and end of the link

            # # Get course id
            req_url = link # "https://ke.qq.com/course/206987"
            split_str = req_url.split("/")
            course_id = split_str[-1] #取得url中的课程id
                    
            itemCourse = KeqqItem()
            itemCourse["course_name"] = course_name
            itemCourse["sold_count"] = sold_count
            itemCourse["price"] = price
            itemCourse["sold_by"] = sold_by
            itemCourse["link"] = link
            itemCourse["cid"] = course_id

            # courses.append(itemCourse)

            # itemList.append(itemCourse)

            logging.debug("[叁] This is a debug message @ page(self, response) course_name : %s" %course_name)
            logging.debug("[叁] This is a debug message @ page(self, response) course_id : %s" %course_id)
            logging.debug("[叁] This is a debug message @ page(self, response) link : %s" %link)
            # item['KeqqItem'] = itemCourse # Add courses
            # yield itemCourse
            logging.debug("going to detail page using yield Request $ ")  
            yield Request(url=link, callback=self.detail, meta={'itemCourse': itemCourse})

        # for detailLink in itemList["KeqqItem"]["link"]:
        #     yield Request(url=detailLink, callback=self.detail)

        logging.debug(" will be the last debug logging @ end of page(self, response)")        
            
    def detail(self, response):
        logging.debug(" I am in @  detail(self, response)")   
        # global itemList # define global variable 
        # itemList = KeqqItemList() # need to move top  
        itemList = KeqqItemList()
        item = response.meta['itemCourse']
        itemList["KeqqItem"] = item

        # Get course basci info<prieviously these info get from list page>
        # Due to the result mixed mess with the other info, move it here
        # course_name = response.xpath("//h1[@class='page-tt']/span[@class='title-main']/text()").extract_first()
        # sold_count  = response.xpath("//div[@class='tt-below-line']/span[@class='line-item statistics-apply']/text()").extract_first()
        # price  = response.xpath("//p[@class='course-price-info ']/span[@class='price ']/span[@class='fontsize-22']/text()").extract_first()
        # sold_by  =  response.xpath("//div[@class='tt-cover-name']/a[@class='tt-link js-agency-name']/text()").extract_first()
        # link = response.url

        # Get course id
        req_url = response.url # "https://ke.qq.com/course/206987"
        logging.debug("This is a debug message @ detail(self, response) link : %s" %req_url)
        split_str = req_url.split("/")
        course_id = split_str[-1] #取得url中的课程id
        print("course_id: ", course_id)

        # itemCourse = KeqqItem()

        # itemCourse["course_name"] = course_name
        # itemCourse["sold_count"] = sold_count
        # itemCourse["price"] = price
        # itemCourse["sold_by"] = sold_by
        # itemCourse["link"] = link
        # itemCourse["cid"] = course_id

        # itemList["KeqqItem"] = itemCourse

        # Course Intro
        intro_tab = response.xpath("//div[@class='tabs-tt-bar js_tab js-tab-nav']/h2[@ref='js_basic_tab']/text()").extract_first()
        content_tab = response.xpath("//div[@class='tabs-tt-bar js_tab js-tab-nav']/h2[@ref='js_dir_tab']/text()").extract_first()
        comment_tab = response.xpath("//div[@class='tabs-tt-bar js_tab js-tab-nav']/h2[@ref='js_comment_tab']/text()").extract_first()
        intro_title =  response.xpath("//div[@class='guide-bd']/table[@class='tb-course']/tbody/tr/th/text()").extract_first()
        intro_detail = response.xpath("//div[@class='guide-bd']/table[@class='tb-course']/tbody/tr/td/text()").extract_first()
        teacher_intro_title = response.xpath("//div[@class='tabs-content']/h3/text()").extract_first() # extract normal generates list, better use extract_first instead
        # termValid = response.xpath("//div[@data-termid='100199073']/p[@class='class-date']/text()").extract_first() # Class available till date
        

        print("intro_tab: ", intro_tab)
        print("intro_title: ", intro_title)
        print("intro_detail: ", intro_detail)
        print("teacher_intro_title: ", teacher_intro_title)

        itemintros = []
        itemIntro = KeqqItemIntro()

        itemIntro["intro_tab"] = intro_tab
        itemIntro["content_tab"] = content_tab
        itemIntro["comment_tab"] = comment_tab
        itemIntro["intro_title"] = intro_title
        itemIntro["intro_detail"] = intro_detail
        itemIntro["teacher_intro_title"] = teacher_intro_title
        itemIntro["cid"] = course_id

        logging.debug("[肆]This is a debug message @ detail(self, response) intro_detail : %s" %intro_detail)

        itemintros.append(itemIntro)

        itemList["KeqqItemIntro"] = itemintros        
        
        # Add itemCourse in the itemList
        # for i in range(len(itemList["KeqqItem"])):
        #     icid = str(courses[i]["cid"])
        #     if str(courses[i]["cid"]) == course_id:
        #         itemList["KeqqItem"] = courses[i]
        #         break      

        #Tecacher List
        itemTeachers = []
        for teach in response.xpath("//div[@class='teacher-list']/div[@class='teacher-item']"):
            teacher_id = teach.xpath("./div[@class='text-right']/h4/a/@href").re_first(r'/teacher/(.*)')
            teacher_name =  teach.xpath("./div[@class='text-right']/h4/a/text()").extract_first()
            teacher_intro = teach.xpath("./div[@class='text-right']/div[@class='text-intro js-teacher-intro']/text()").extract_first()
            # course_url = response.url

            itemTeacher = KeqqItemTeacher()

            itemTeacher["teacher_id"] = teacher_id
            itemTeacher["teacher_name"] = teacher_name
            itemTeacher["teacher_intro"] = teacher_intro
            itemTeacher["cid"] = course_id
            # itemTeacher["course_url"] = course_url
            logging.debug("[伍]This is a debug message @ detail(self, response) teacher_name : %s" %teacher_name)

            itemTeachers.append(itemTeacher)
        
        itemList["KeqqItemTeacher"] = itemTeachers

        # Get class table contents
        courseTableContent =  response.xpath("//body").re(r'metaData\s=\s{*(.*)};') # response.xpath("//body").re(r'metaData\s=\s*(.*)};')
        strCourse = str(courseTableContent[0])
        strCourse = "{"+strCourse+"}"
        #
        regex = re.compile(r'\\(?![/u"])')  
        fixed = regex.sub(r"\\\\", strCourse)  
        #
        # jdata = json.loads(strCourse)
        jdata = json.loads(fixed)

        course_name = jdata["name"]
        print("course_name: %s"%course_name)

        itemTerms = []
        itemChapters = []
        itemSubInfos = []
        itemTaskInfos = []

        for i in range(len(jdata["terms"])):
            term_Name = jdata["terms"][i]["name"]
            term_id = jdata["terms"][i]["term_id"]
            term_cid = jdata["terms"][i]["cid"]
            term_aid = jdata["terms"][i]["aid"]

            itemTerm = KeqqItemTerm()

            itemTerm["term_Name"] = term_Name
            itemTerm["term_id"] = term_id
            itemTerm["term_cid"] = term_cid
            itemTerm["term_aid"] = term_aid
            logging.debug(" [陆]This is a debug message @ detail(self, response) term_Name : %s" %term_Name)

            itemTerms.append(itemTerm)

            for ichapter in range(len(jdata["terms"][i]["chapter_info"])):
                chapter_term_id = jdata["terms"][i]["chapter_info"][ichapter]["term_id"]
                chapter_aid = jdata["terms"][i]["chapter_info"][ichapter]["aid"]
                chapter_ch_id = jdata["terms"][i]["chapter_info"][ichapter]["ch_id"]
                chapter_cid = jdata["terms"][i]["chapter_info"][ichapter]["cid"]
                # print("chapter_term_id: %s chapter_aid : %s chapter_ch_id: %s chapter_cid %s "%(chapter_term_id, chapter_aid, chapter_ch_id, chapter_cid))

                itemChapter = KeqqItemChapter()

                itemChapter["chapter_term_id"] = chapter_term_id
                itemChapter["chapter_aid"] = chapter_aid
                itemChapter["chapter_ch_id"] = chapter_ch_id
                itemChapter["chapter_cid"] = chapter_cid

                logging.debug(" [柒]This is a debug message @ detail(self, response) chapter_term_id : %s" %chapter_term_id)

                itemChapters.append(itemChapter)

                for isub in range(len(jdata["terms"][i]["chapter_info"][ichapter]["sub_info"])):
                     sub_info_term_id = jdata["terms"][i]["chapter_info"][ichapter]["sub_info"][isub]["term_id"]
                     sub_info_csid = jdata["terms"][i]["chapter_info"][ichapter]["sub_info"][isub]["csid"]
                     sub_info_cid = jdata["terms"][i]["chapter_info"][ichapter]["sub_info"][isub]["cid"]
                     sub_info_sub_id = jdata["terms"][i]["chapter_info"][ichapter]["sub_info"][isub]["sub_id"] + 1
                     sub_info_sub_id = "%02d" % sub_info_sub_id
                     sub_info_name = str(sub_info_sub_id) + " " + jdata["terms"][i]["chapter_info"][ichapter]["sub_info"][isub]["name"]
                    
                     itemSubInfo = KeqqItemSubInfo()

                     itemSubInfo["sub_info_term_id"] = sub_info_term_id
                     itemSubInfo["sub_info_csid"] = sub_info_csid
                     itemSubInfo["sub_info_cid"] = sub_info_cid
                     itemSubInfo["sub_info_sub_id"] = sub_info_sub_id
                     itemSubInfo["sub_info_name"] = sub_info_name

                     logging.debug("[捌]This is a debug message @ detail(self, response) sub_info_name : %s" %sub_info_name)

                     itemSubInfos.append(itemSubInfo)

                     for itask in range(len(jdata["terms"][i]["chapter_info"][ichapter]["sub_info"][isub]["task_info"])):

                        task_info_name = jdata["terms"][i]["chapter_info"][ichapter]["sub_info"][isub]["task_info"][itask]["name"]
                        task_info_term_id = jdata["terms"][i]["chapter_info"][ichapter]["sub_info"][isub]["task_info"][itask]["term_id"]
                        task_info_csid = jdata["terms"][i]["chapter_info"][ichapter]["sub_info"][isub]["task_info"][itask]["csid"]
                        task_info_aid = jdata["terms"][i]["chapter_info"][ichapter]["sub_info"][isub]["task_info"][itask]["aid"]
                        task_info_cid = jdata["terms"][i]["chapter_info"][ichapter]["sub_info"][isub]["task_info"][itask]["cid"]
                        task_info_taid = jdata["terms"][i]["chapter_info"][ichapter]["sub_info"][isub]["task_info"][itask]["taid"]

                        itemTaskInfo = KeqqItemTaskInfo()                        
                        itemTaskInfo["task_info_name"] = task_info_name
                        itemTaskInfo["task_info_term_id"] = task_info_term_id
                        itemTaskInfo["task_info_csid"] = task_info_csid
                        itemTaskInfo["task_info_aid"] = task_info_aid
                        itemTaskInfo["task_info_cid"] = task_info_cid
                        itemTaskInfo["task_info_taid"] = task_info_taid

                        logging.debug("[玖]This is a debug message @ detail(self, response) task_info_name : %s" %task_info_name)

                        itemTaskInfos.append(itemTaskInfo)

        # Add table contents 
        itemList["KeqqItemTerm"] = itemTerms
        itemList["KeqqItemChapter"] = itemChapters
        itemList["KeqqItemSubInfo"] = itemSubInfos
        itemList["KeqqItemTaskInfo"] = itemTaskInfos

          
        #  Get comments 
        print("Starting to fetch comments ....")
       
        # course_id = '206987' #course_id
        url = "https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid="+course_id+"&count=10&page=0&filter_rating=0&bkn=&r=0.1975509950404375"
        header = {
            ':authority':'ke.qq.com',
            ':method':'GET',
            'referer':'https://ke.qq.com/course/'+course_id+'',
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
            'x-requested-with':'XMLHttpRequest'
            }

        yield Request(url=url, callback=self.getComment, headers=header, meta={'itemList':itemList})
        # return itemList
       
    def getComment(self, response):
        # global item # reassure global variable 
        itemList = response.meta['itemList']
        print("Inside getComment ....")
        result = response.body.decode('utf-8','ignore')
        comment = json.loads(result)
        
        # If there are comment sections
        if len(comment["result"]["items"]) > 0 :
            itemComments = []
            for i in range(len(comment["result"]["items"])):
                nick_name  =  comment["result"]["items"][i]["nick_name"]
                userid = comment["result"]["items"][i]["id"] 
                first_comment_score = comment["result"]["items"][i]["first_comment_score"] # 评论星数
                first_comment_time = comment["result"]["items"][i]["first_comment_time"] # 评论时间
                first_comment_progress = comment["result"]["items"][i]["first_comment_progress"] # 评论时间
                rating = comment["result"]["items"][i]["rating"] # 评分
                cid = comment["result"]["items"][i]["cid"] # 课程id
                first_comment =  comment["result"]["items"][i]["first_comment"] # 评论内容

                try:
                    # if len(comment["result"]["items"][i]) < 10 :
                    #     first_reply ="No comment"
                    # else:
                    #     print("I am in else ")
                    #     first_reply = comment["result"]["items"][i]["first_reply"] # 评论回复

                    if "first_reply" in comment["result"]["items"][i]:
                        print("I am in else ")
                        first_reply = comment["result"]["items"][i]["first_reply"] # 评论回复
                    else:
                        first_reply ="No comment"   

                except Exception as ex:
                    print("Errors #### @:",str(ex.message))

                itemComment = KeqqItemComment()

                itemComment["nick_name"] = nick_name
                itemComment["userid"] = userid
                itemComment["first_comment_score"] = first_comment_score
                itemComment["first_comment_time"] = first_comment_time
                itemComment["first_comment_progress"] = first_comment_progress
                itemComment["rating"] = rating  
                itemComment["cid"] = cid
                itemComment["first_comment"] = first_comment
                itemComment["first_reply"] = first_reply

                logging.debug("[拾]This is a debug message @ getComment(self, response) nick_name : %s and comment: %s" %(nick_name, first_comment))

                itemComments.append(itemComment)    
            print("Adding comment sections...")
            # Put comment sections data in the item
            itemList["KeqqItemComment"] = itemComments
        
        # listCourse.append(itemList)
        # 返回所有的数据        
        yield itemList
           
def savefield(fieldValue): 
    # 普通方法不需要空格后再写，否则在调用的地方会找不到方法
    filepath = "C:/Users/IBM_ADMIN/crawlers/ke.txt"

    # if flag =="del":
        # if os.path.exists(filepath):
        #     print("Ready to remove file....")
        #     os.remove(filepath)
        # else:
        #     print("File doesn't exist")

    with open(filepath,'a', encoding='gbk', errors='ignore') as f:
        f.write(fieldValue)
        f.write("\n")
        f.write("-" * 100 + "\n")
        # print("Successfully write to disk")

   

# https://www.zhihu.com/question/28981353
# https://zhuanlan.zhihu.com/p/20920903?refer=data-factory
# https://ithelp.ithome.com.tw/articles/10094915
# https://doc.phpspider.org/callback.html
# http://blog.csdn.net/u011781521/article/details/70210364
# https://www.weibo.com/ttarticle/p/show?id=2309404103266454643821&infeed=1
# http://www.jianshu.com/p/4fe8bb1ea984 获取并加载数据
# https://zhidao.baidu.com/question/1499356415053936779.html 如何利用python读取网页中变量的内容
# http://blog.chinaunix.net/uid-23500957-id-3788157.html
# http://m.blog.csdn.net/sqc157400661
# https://stackoverflow.com/questions/27726506/scrapy-visiting-nested-links-and-grabbing-meta-data-from-each-level 