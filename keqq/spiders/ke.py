# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.http import Request
from keqq.items import KeqqItem




class KeSpider(scrapy.Spider):
    name = 'ke'
    allowed_domains = ['ke.qq.com']
    start_urls = ['http://ke.qq.com/']
    print("before parse###")

    def parse(self, response):
        print("This is the start of response --------------------------")
        # result = response.body.decode('utf-8', 'ignore')
        print(response.xpath("//title/text()").extract())
        # print('what is the result: ',result)
        # logging.log(logging.WARNING, "----" * 200)
        # logging.log(logging.WARNING, "###: " + result)
        # logging.log(logging.WARNING, "----" * 200)

        key = "python"
        for i in range(1,2):
            url = "https://ke.qq.com/course/list/"+str(key)+"?page="+str(i)

        yield Request(url=url, callback=self.page)


    def page(self, response):
        # response.xpath("//h4[@class='item-tt']/a[@class='item-tt-link']/text()").extract()
        # course_name  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/h4[@class='item-tt']/a[@class='item-tt-link']/text()").extract()
        # sold_count  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--middle']/span[@class='line-cell item-user']/text()").extract()
        # price  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--bottom']/span[@class='line-cell item-price']/text()").extract()
        # sold_by  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--middle']/span[@class='item-source']/a[@class='item-source-link']/text()").extract()

        # list_courses = []

        for course in response.xpath("//div[@class='main-left']/div[@class='market-bd market-bd-6 course-list course-card-list-multi-wrap']/ul[@class='course-card-list']/li[@class='course-card-item']"):
            course_name = course.xpath("./h4[@class='item-tt']/a[@class='item-tt-link']/text()").extract_first()
            sold_count  = course.xpath("./div[@class='item-line item-line--middle']/span[@class='line-cell item-user']/text()").extract_first()
            price  = course.xpath("./div[@class='item-line item-line--bottom']/span[@class='line-cell item-price']/text()").extract_first()
            sold_by  = course.xpath("./div[@class='item-line item-line--middle']/span[@class='item-source']/a[@class='item-source-link']/text()").extract_first()
            link = "https:" + str(course.xpath("./a/@href").extract_first()).strip() # Remove space in front and end of the link

            #For Debug purpose #
            print("course_name ##: ", course_name)
            print("sold_count ##: ", sold_count)
            print("price ##: ", price)
            print("sold_by ##: ", sold_by)
            print("link ##: ", link)

            logging.log(logging.WARNING, "course_name ##: " + course_name)
            logging.log(logging.WARNING, "sold_count ##: " + sold_count)
            logging.log(logging.WARNING, "price ##: " + str(price))
            logging.log(logging.WARNING, "sold_by ##: " + sold_by)
            logging.log(logging.WARNING, "link ##: " + link)


            # a_course = []
            # a_course.append(course_name)
            # a_course.append(sold_count)
            # a_course.append(price)
            # a_course.append(sold_by)
            # a_course.append(link)

            # logging.log(logging.WARNING, "####" * 100)
            # logging.log(logging.WARNING, a_course)
            # logging.log(logging.WARNING, "----" * 100)

            # list_courses.append(a_course)
            #For Debug purpose #
            item = KeqqItem()
            item["course_name"] = course_name
            item["sold_count"] = sold_count
            item["price"] = price
            item["sold_by"] = sold_by
            item["link"] = link

            yield Request(url=link, callback=self.detail)

        # logging.log(logging.WARNING, "###All Courses###")
        # logging.log(logging.WARNING,list_courses)

    def detail(self, response):
        title = response.xpath("//title/text()").extract()
        intro_title =  response.xpath("//div[@class='guide-bd']/table[@class='tb-course']/tbody/tr/th/text()").extract()
        intro_detail = response.xpath("//div[@class='guide-bd']/table[@class='tb-course']/tbody/tr/td/text()").extract()
        teach_section = response.xpath("//div[@class='tabs-content']/h3/text()").extract()

        print("Course Detail Title: ", title)
        print("intro_title: ", intro_title)
        print("intro_detail: ", intro_detail)
        print("teach_section: ", teach_section)

        logging.log(logging.WARNING, "Course Detail Title: " + str(title))
        logging.log(logging.WARNING, "intro_title: " + str(intro_title))
        logging.log(logging.WARNING, "intro_detail: " + str(intro_detail))
        logging.log(logging.WARNING, "teach_section: " + str(teach_section))

         #Table Content
        logging.log(logging.WARNING,"############--Sart of Table Content") 
        for content in response.xpath("//div[@class='task-chapter']/div[@class='task-part-list']/div[@class='task-part-item']"):
            chapter_no = content.xpath("./div[@class='task-part-hd']/span/text()").extract()
            chapter_name = content.xpath("./div[@class='task-part-hd']/h3/text()").extract()

            logging.log(logging.WARNING,"############--Table Content")    

            logging.log(logging.WARNING, "chapter_no + chapter_name: " + chapter_no  + chapter_name)
            
            for task in content.xpath("./div[@class='task-task-list']"):
                task_name = task.xpath("./a[@class='task-task-item task-item-jump js-expr-video-link js-task-without-login js-expr-item']/p[@class='task-tt']/span[@class='task-tt-text']/text()").extract()
                task_duration = task.xpath("./a[@class='task-task-item task-item-jump js-expr-video-link js-task-without-login js-expr-item']/p[@class='task-tt']/span[@class='tt-suffix']/text()").extract()
                logging.log(logging.WARNING, "task_name + task_duration: " + task_name  + task_duration)

        logging.log(logging.WARNING,"############--End of Table Content") 

        #Tecacher List
        for teach in response.xpath("//div[@class='teacher-list']/div[@class='teacher-item']"): #no extract() needed 
            teacher_name =  teach.xpath("./div[@class='text-right']/h4/a/text()").extract_first()
            teacher_intro = teach.xpath("./div[@class='text-right']/div[@class='text-intro js-teacher-intro']/text()").extract_first()
            course_url = response.url

            print("teacher_name: ", teacher_name)
            print("teacher_intro: ", teacher_intro)
            print("course_url: ", course_url)

            logging.log(logging.WARNING, "teacher_name: " + teacher_name)
            logging.log(logging.WARNING, "teacher_intro: " + teacher_intro)
            logging.log(logging.WARNING, "course_url: " + course_url)

        logging.log(logging.WARNING,"############--End Teacher List")            

       
            
