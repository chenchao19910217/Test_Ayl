from selenium import webdriver
from selenium.webdriver.chrome.options import Options # => 引入Chrome的配置
import time

# 配置
ch_options = Options()
ch_options.add_argument("--headless")  # => 为Chrome配置无头模式

# 在启动浏览器时加入配置
driver = webdriver.Chrome(options=ch_options) # => 注意这里的参数

driver.get('https://douchacha.com/')
# driver.find_element_by_id('kw').send_keys('测试')
# driver.find_element_by_id('su').click()

time.sleep(2)

# 只有截图才能看到效果咯
driver.save_screenshot('./ch.png')

driver.quit()