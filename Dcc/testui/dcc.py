from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import time
import traceback
import unittest
from Test_Ayl import settings
from core.core import Core
BUGURL = settings.URL+'static/bugpng/'
BUG = settings.BASE_DIR+'/Dcc/static/bugpng/'


class Selenium_PC(unittest.TestCase):

    def runTest(self):
        self.test_login()
        pass

    def test_login(self):
        doc = '''
            PC首页登录功能，寻找首页登录按钮，账号登录，账号：15512090218 ，密码：cc123456x
        '''
        chrome_options = Options()
        chrome_options.add_argument('no-sandbox')
        # 无头模式
        chrome_options.add_argument('headless')
        # 无头模式element不可交互问题
        # chrome_options.add_argument("window-size=1920,1080")
        # 初始化浏览器
        self.web_opt = webdriver.Chrome(options=chrome_options)
        # self.web_opt = webdriver.Chrome()
        # 请求首页
        self.web_opt.get('https://baidu.com')
        # 等待元素加载
        self.web_opt.implicitly_wait(3)
        try:
            # 点击登录
            self.web_opt.find_element_by_xpath(
                '//*[@class="el-button header_button_main gradient_button gradient_bule el-button--info is-round"]').click()
            # 切换登录方式
            self.web_opt.find_element_by_xpath('//*[@class="login_dialog_switch"]').click()
            # 输入账号
            self.web_opt.find_element_by_xpath('//*[@placeholder="请输入手机号"]').send_keys(15512090218)
            # 输入密码
            self.web_opt.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys('cc123456x')
            # 登录
            self.web_opt.find_element_by_xpath('//*[@class="el-button login_button el-button--primary"]').click()
            # 通过个人中心元素验证登录是否成功
            self.web_opt.find_element_by_xpath('//*[@class="el-avatar el-avatar--circle 1"]')
        except:
            # 出现错误进行截图
            name=sys._getframe().f_code.co_name + time.strftime("%Y%m%d%H%M%S") + '.png'
            self.web_opt.get_screenshot_as_file(BUG + name)
            bugurl = BUGURL+ name
            mail = Core()
            content = '报错功能：'+doc+'报错地址：'+bugurl
            mail.send_mail(content)

        # 关闭浏览器
        self.web_opt.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
