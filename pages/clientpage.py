'''客户资料'''
from selenium import webdriver
from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

from common.loggen import Loggen
logger = Loggen(logger='ClientPage').getlog()

class ClientPage(BasePage):
    meetingcode = (By.CSS_SELECTOR,'[placeholder="请输入场次编号"]')
    usercode = (By.CSS_SELECTOR,'[placeholder="请输入账号"]')
    userpwd = (By.CSS_SELECTOR,'[placeholder="请输入密码"]')
    loginbn=(By.XPATH,'//*[@id="app"]/div/div/div[1]/div/form/div[4]/div/button')
    clientlist = (By.XPATH, '/html/body/div/div/div/div/div/div/div/div/ul/div/li[2]')
    client = (By.XPATH, '/html/body/div/div/div/div/div/div/div/div/ul/div/li[2]/ul/li[1]/span')
    client_add=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/ul/div/div/button[1]')
    client_add_area=(By.XPATH,'/html/body/div/div/div/div/div/div/div/div/div/div/div/div/form/div/div/div/div/div/div/div/div/div/div/input[1]')
    client_add_area_Regionname=(By.XPATH,'//*[@id="cascader-menu-3415-0-1"]/span')
    client_add_area_Agentname=(By.XPATH,'/html/body/div/div/div/div/ul/li/span[last()]')
    client_add_area_Dealename=(By.XPATH,'/html/body/div/div/div/div/ul/li/span[last()]')
    client_add_Shop=(By.XPATH,'/html/body/div/div/div/div/div/div/div/div/div/div/div/div/form/div/div/div/div/div/div/div/div/div/input[2]')
    client_add_Shopname = (By.XPATH,'/html/body/div/div/div/div/div/div/div/div/div/div/div/div/form/div/div/div/div/div/div/div/div/div/input[3]')
    client_add_preservationbn=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/div/div[3]/div/div[3]/div/button[2]')



    # 定义密码元素识别及输入函数，并将此操作写入日志
    def input_meetingcode(self,meetingcode):
        self.find_element(*self.meetingcode).send_keys(meetingcode)
        logger.info("输入场次：%s." %meetingcode)

    def input_usercode(self, usercode):
        self.find_element(*self.usercode).send_keys(usercode)
        logger.info("输入用户名：%s." % usercode)

    def input_userpwd(self, userpwd):
        self.find_element(*self.userpwd).send_keys(userpwd)
        logger.info("输入密码：%s." % userpwd)
        time.sleep(2)

    def input_loginbn(self):
        self.find_element(*self.loginbn).click()
        logger.info("点击登录")
        time.sleep(2)

    def input_clientlist(self):
        self.find_element(*self.clientlist).click()
        self.find_element(*self.client).click()
        logger.info("点击客户资料-店铺资料菜单")
        time.sleep(2)

    def input_client_add(self):
        self.find_element(*self.client_add).click()
        logger.info("添加店铺")
        self.find_element(*self.client_add_area).click()
        self.find_element(*self.client_add_area_Regionname).click()  # 归属区域
        self.find_element(*self.client_add_area_Agentname).click()
        self.find_element(*self.client_add_area_Dealename).click()
        self.find_element(*self.client_add_Shop).send_keys('10000')  #店铺编号
        self.find_element(*self.client_add_Shopname).send_keys('店铺10000')   #店铺名称
        self.find_element(*self.client_add_preservationbn).click()     # 保存
        logger.info("添加店铺10000")

        time.sleep(2)







