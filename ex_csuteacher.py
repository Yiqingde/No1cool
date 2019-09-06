# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:26:47 2019

@author: yiqing
"""

import re#python正则分割
from  bs4 import BeautifulSoup#网页美味汤
#from selenium import webdriver#模拟点击鼠标点击网页库
#import time#时间
import  requests#直接爬取网页库
'''
#--------------------------------------搜索中南大学教师主网页
def search_school(url,chromedrive):
    browser= webdriver.Chrome(chromedrive)
    browser.get(url)
    #开始定位至学院列表 休息15s
    browser.find_element_by_link_text("学院列表").click()
    time.sleep(5)
    return browser

#--------------------------------------由二级学院开始进行网上搜索
def search_2school(school,browser):
    browser.find_element_by_link_text(school).click()#开始定位至地信院 休息15s
    time.sleep(15)
    #承接内容 使用pytho"n正则表达式 将老师的网址找到并存至gg中
    html = browser.page_source
    rule="http://faculty.csu.edu.cn/.*/zh_CN/index.htm"
    gg=re.findall(rule,html)
    return gg
'''
#--------------------------------------由二级学院开始进行网上搜索
def direct(secname):
    r=requests.get(secname)
    html=r.text
    rule="http://faculty.csu.edu.cn/.*/zh_CN/index.htm"
    gg=re.findall(rule,html)
    return gg
#--------------------------------------将个人主页内容爬出来
def div(gg_i):
    str="  该老师爬不了!!!  点击网页链接访问"
    r=requests.get(gg_i)
    soup=BeautifulSoup(r.text,"lxml")
    div=soup.find("div",attrs={"class":"TabbedPanelsContent"})   
    if div==None:
        div=soup.find("div", class_="jiancc")
    if div==None:
        div=soup.find("div",attrs={"class":"con_bload"})
    if div==None:
        div=soup.find("div",attrs={"class":"teacher_mid_midL_bot fl"})
    if div==None:
        return str
    else:
        return div.text
#--------------------------------------写入指定文件 filename为路径 gg为存储的网址
def write(filename,gg):
    f= open(filename,'w',encoding='utf-8')
    for i in range(len(gg)):
        f.write("\r\n")
        taglink="第"+str(i+1)+"个老师的网页位置:"+gg[i]
        f.write(taglink)
        f.write(div(gg[i]))
        f.write("\r\n")
        print(i+1)  
#--------------------------------------替换str中的[]符号
def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*_-+=<>?/,.:;{}[]|\'""":
            line = line.replace(ch, "")
    return line
#--------------------------------------获取学院名字
def txt_name(number):
    all_colleage="http://faculty.csu.edu.cn/xueyuan.jsp?urltype=tree.TreeTempUrl&wbtreeid=1014"
    r1=requests.get(all_colleage)
    rule1="urltype=tsites.CollegeTeacherList&wbtreeid=1014&tscollegeid=10"+number+"\">(.*)</a></li>"
    colleage_name=re.findall(rule1,r1.text)
    return colleage_name
#--------------------------------------main()
def main():
    #chromedrive = 'D:\Program Files (x86)\Google\Chrome\Application\chromedriver'
    #browser=search_school(url,chromedrive)
    secname_1="http://faculty.csu.edu.cn/xyjslist.jsp?urltype=tsites.CollegeTeacherList&wbtreeid=1014&tscollegeid=10"
    for i in range(34):
        if i<9:
            number="0"+str(i+1)
        else:
            number=str(i+1)
        secnameurl=secname_1+number#储存各个学院的网址
        #gg=search_2school(secname,browser)
        gg=direct(secnameurl)#直接访问 网页内容储存至gg中
        print(replacePunctuations(str(txt_name(number))))#打印正在记录的文件
        filename="D:\\"+replacePunctuations(str(txt_name(number)))+'.txt'
        print(filename)
        write(filename,gg)#写文件 
main()
   


