# 读取驱动文件
#-*- coding: UTF-8 -*-
from common.ReadConfig import getbrowserinfo
from selenium import webdriver
from common.cappic import Cappic
from common.loggen import Loggen
logger=Loggen(logger='浏览器启动加载').getlog()
import os
from common.cappic import Cappic
def BrowserStart():
    browsername=getbrowserinfo('BrowserName')
    url=getbrowserinfo('url')
    if browsername=='fierfor':
        logger.info('启动firefox浏览器')
        driver=webdriver.Firefox()
        logger.info('打开测试网页')
        driver.get(url)
    if browsername=='chrome':
        logger.info('启动chrome浏览器')
        driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        driver.get(url)
        logger.info('打开测试网页')
BrowserStart()

