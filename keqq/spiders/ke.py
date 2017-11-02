# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.http import Request
from lxml import etree




class KeSpider(scrapy.Spider):
    name = 'ke'
    allowed_domains = ['ke.qq.com']
    start_urls = ['http://ke.qq.com/']
    print("before parse###")

    def parse(self, response):
        print("This is the end of code --------------------------")
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
        course_name  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/h4[@class='item-tt']/a[@class='item-tt-link']/text()").extract()
        sold_count  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--middle']/span[@class='line-cell item-user']/text()").extract()
        price  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--bottom']/span[@class='line-cell item-price']/text()").extract()
        sold_by  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--middle']/span[@class='item-source']/a[@class='item-source-link']/text()").extract()

        list_courses = []

        for course in response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']"):
            course_name = course.xpath("./h4[@class='item-tt']/a[@class='item-tt-link']/text()").extract_first()
            sold_count  = course.xpath("./div[@class='item-line item-line--middle']/span[@class='line-cell item-user']/text()").extract_first()
            price  = course.xpath("./div[@class='item-line item-line--bottom']/span[@class='line-cell item-price']/text()").extract_first()
            sold_by  = course.xpath("./div[@class='item-line item-line--middle']/span[@class='item-source']/a[@class='item-source-link']/text()").extract_first()

            print("course_name ##: ", course_name)
            print("sold_count ##: ", sold_count)
            print("price ##: ", price)
            print("sold_by ##: ", sold_by)

            a_course = []
            a_course.append(course_name)
            a_course.append(sold_count)
            a_course.append(price)
            a_course.append(sold_by)

            logging.log(logging.WARNING, "####" * 100)
            logging.log(logging.WARNING, a_course)
            logging.log(logging.WARNING, "----" * 100)

            list_courses.append(a_course)

        logging.log(logging.WARNING, "###All Courses###")
        logging.log(logging.WARNING,list_courses)      


