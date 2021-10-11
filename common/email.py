# 连接发送邮件的库
import  smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

import os
#设置环境变量的库
import sys
import time

def new_file():
    current_path=os.path.abspath(os.path.join(os.path.dirname('settings.py'),os.path.pardir)) # 获取当前路径
    # 列举report 目录下所有文件，结果以列表形式返回
    path = (current_path+"\\report" )
    lists = os.listdir(path)