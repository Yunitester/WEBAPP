from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from common.loggen import Loggen
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
loggen = Loggen(logger="MainPage").getlog()
# 定义主页面中所涉及到的元素，userid及退出按钮，通过xpath方式识别
class MainPage(BasePage):
    userid_loc=(By.XPATH,"//*[@id=\"app\"]/div/div[1]/div[3]/div/span")
    exit_btn_loc1=(By.CSS_SELECTOR,"[class=\"el-dropdown-link el-dropdown-selfdefine\"]")
    exit_btn_loc2=(By.XPATH,"/html/body/div[2]/div/div[3]/button[2]/span")
    eldowm=(By.CLASS_NAME,"el-dropdown")
    # 定义显示userid信息，并将此操作写入日志
    def show_userid(self):
        userid=self.find_element(*self.userid_loc).text
        loggen.info("当前用户id是：%s."%userid)
        return userid
    #定义退出操作，点击退出按钮，并将此操作写入日志
    def exit_sys(self):
        ac = ActionChains(self.driver)  # driver 是 web 对象
        # 鼠标移动到元素
        ac.move_to_element(
            self.find_element(*self.eldowm)
        ).perform()
        self.find_element(*self.exit_btn_loc1).click
        self.find_element(*self.exit_btn_loc2).click
        loggen.info("退出系统")