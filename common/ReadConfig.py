
import configparser
import os
def  getbrowserinfo(name):
    cf=configparser.ConfigParser()
   #cfpath=os.path.dirname(os.path.abspath('.'))  # abspath获取当前路径，dirname获取上一层
    cfpath=os.path.dirname(os.path.abspath('.')) +'\\config\\in.ini'
    cf.read(cfpath)
    browserinfo=cf.get('browser',name)
    return  browserinfo


