from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import traceback
import unittest





class Test_Selenium(unittest.TestCase):
    

    def setUp(self) -> None:
        chrome_options = Options()
        # # 无头模式
        # chrome_options.add_argument('--headless')
        # # 无头模式element不可交互问题
        # chrome_options.add_argument("--window-size=4000,1600")
        # # 手机模式
        mobileEmulation = {'deviceName': 'iPhone X'}
        chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)

        self.web_opt = webdriver.Chrome(options=chrome_options)
        # self.web_opt = webdriver.Chrome()
        self.web_opt.get('https://www.douchacha.com')

    def test_find_element(self):
        tt="aaaaaaaaaaaaaaaaaaaaaaaaaa"
        try:
            print(self.web_opt.get_screenshot_as_file('./aaa.png'))
            ele = self.web_opt.find_element_by_xpath(
                '//*[@class="el-button header_button_main gradient_button gradient_bule el-button--info is-round"]')
            ele.click()
            ele1 = self.web_opt.find_element_by_xpath('//*[@class="login_dialog_switch"]')
            ele1.click()
            self.web_opt.find_element_by_xpath('//*[@placeholder="请输入手机号"]').send_keys(15512090218)
            self.web_opt.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys('cc123456x')
            ele4 = self.web_opt.find_element_by_xpath('//*[@class="el-button login_button el-button--primary"]')
            ele4.click()
            time.sleep(3)
            res2 = self.web_opt.find_element_by_xpath('//*[@class="el-avatar el-avatar--circle"]')
            self.assertTrue(res2, msg='登录失败')
            self.web_opt.get_screenshot_as_file('./bbb.png')
        except:
            print(traceback.format_exc())

        self.web_opt.close()

    def runTest(self):
        pass


if __name__ == '__main__':
    unittest.main()
