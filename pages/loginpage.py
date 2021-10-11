#-*- coding: UTF-8 -*

from pages.basepage import BasePage
from common.loggen import Loggen

from selenium.webdriver.common.by import By

import time
logger = Loggen(logger='LoginPage').getlog()

class LoginPage(BasePage):
    users = (By.XPATH,'//*[@id="nav_pwuser"]')
    userpwd = (By.CSS_SELECTOR,'[name="pwpwd"]')
    loginbn = (By.CSS_SELECTOR,'[name="head_login"]')
    username = (By.CSS_SELECTOR,'[href="u.php"]')
    closebn = (By.CSS_SELECTOR,'[class="fr menu_close"]')


    # 定义密码元素识别及输入函数，并将此操作写入日志

    def input_users (self,users):
        self.find_element(*self.users).send_keys(users)
        logger.info("用户名：%s."%users)

    def input_userpwd(self, userpwd):
        self.find_element(*self.userpwd).send_keys(userpwd)
        logger.info("输入密码：%s." % userpwd)

    def input_loginbn(self,):
        self.find_element(*self.loginbn).click()
        logger.info("点击登录按钮")


    def input_closebn(self,):
        self.find_element(*self.closebn).click()
        logger.info("关闭页面弹框")

    '''def input_username(self):
        a = self.find_element(*self.username).text
        if a == "":
            print('成功')

        else:
            print("失败")
      
        self.find_element(*self.usercode).click()
        logger.info("点击个人资料")
        if self.usercode.text == self.users.text:
            logger.info('登录成功')
            # self.logout()  # 调用退出登录参数
        else:
            logger.info('登录成功')
            self.driver.quit()
'''





