# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:23:00 2019
用来刷CSU教师主页热度  每天可刷2000左右 无代理
@author: yiqing
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:54:49 2019

@author: yiqing
"""

# -*- coding:UTF-8 -*-
#!/usr/bin/env python3
 
import re#python正则分割
from  bs4 import BeautifulSoup#网页美味汤
from selenium import webdriver#模拟点击鼠标点击网页库
import time#时间
import  random#直接爬取网页库
def hot(i,browser):
    url="http://faculty.csu.edu.cn/zuotingying/*****/index.htm"
    while True:
        #browser.get(url[random.randint(0,5)])
        #time.sleep(random.randint(3,10))
        browser.get(url)
        i=i+1
        print(i)
 
if __name__ == "__main__":
    chromedrive = 'D:\Program Files (x86)\Google\Chrome\Application\chromedriver'
    browser= webdriver.Chrome(chromedrive)
    i=50
    hot(50,browser)