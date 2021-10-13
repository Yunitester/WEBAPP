# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime,date,timedelta


# 以下为定义函数部分，其目的是返回今天后第n天的日期，格式为“2021-10-11”
def data_n(n):
    return str((date.today() + timedelta(days= +int(n))).strftime("%Y-%m-%d"))

from_station = "上海"
to_station = "杭州"
# 以下为tomorrow变量
tomorrow= data_n(2)
print(tomorrow)


driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://trains.ctrip.com/")



driver.find_element_by_id('label-departStation').send_keys(from_station)
time.sleep(1)
driver.find_element_by_id('label-arriveStation').send_keys(to_station)
time.sleep(1)

# 移除出发时间的’readonly‘只读属性
#driver.execute_script("document.getElementById('departDate').removeAttribute('readonly')")
#time.sleep(2)

# 清除出发时间默认内容
driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/strong[1]").clear()
time.sleep(2)
driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]/strong[1]").send_keys(tomorrow)
time.sleep(2)

# 以下步骤是为了解决日期控件弹出窗在输入日期后无法消失的问题，以防影响测试进行
#原理是为了让鼠标左键单击页面空白处
ActionChains(driver).move_by_offset(0,0).click().perform()

element1= driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[2]/button')
driver.execute_script("arguments[0].click();",element1)
time.sleep(2)
# 点击“预定”按钮订票
#driver.find_element_by_xpath('/html/body/div[7]/div/div[5]/div[3]/div/div[1]/div[6]/div[1]/a').click()
driver.quit()