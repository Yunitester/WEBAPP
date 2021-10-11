# 截图
import os
import time

def Cappic(driver):
    pt=time.strftime('%Y%m%d%H%M',time.localtime(time.time())) # 时间格式
    picname = os.path.dirname(os.path.abspath('.')+'\\picture\\' +pt+ '.png' )  # 图片路径
    driver.get_screenshot_as_file(picname)