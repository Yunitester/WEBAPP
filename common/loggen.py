#  输出日志
#-*- coding: UTF-8 -*-
import logging
import os
import time
class Loggen(object):
    def __init__(self,logger):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)   # 设置级别

        lt=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        logname=os.path.dirname(os.path.abspath('.'))+'\\WEBTEST\\Logs\\'+lt+'.log'
        #logname='D:\\PycharmProjects\\WEBTEST\\Logs'+lt+'.log'
        fileh = logging.FileHandler(logname)
        fileh.setLevel(logging.INFO)

        consoleh=logging.StreamHandler()
        consoleh.setLevel(logging.INFO)

        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileh.setFormatter(formatter)
        consoleh.setFormatter(formatter)
        self.logger.addHandler(fileh)
        self.logger.addHandler(consoleh)
    def getlog(self):
        return self.logger

