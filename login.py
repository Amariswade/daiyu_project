import selenium
import setting
import time
from selenium import webdriver
class Login(object):
    def __init__(self):
        self.url = setting.channel_web_url+'/login'
        self.name = None
        self.pwd = None
        self.sub = None
    def get_driver(self):
        chrome = webdriver.Chrome()
        chrome.get(self.url)
        time.sleep(1)
        chrome.maximize_window()
        self.driver = chrome
    def find_ele(self):
        self.name = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div/input')
        self.pwd = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[3]/div/div/input')
        self.sub = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/form/button')
    def set_value(self):
        self.name.clear()
        self.name.send_keys('13999999990')
        self.pwd.clear()
        self.pwd.send_keys('a123456')
        self.sub.click()
        time.sleep(1)
    def run(self):
        self.get_driver()
        self.find_ele()
        self.set_value()
        if(self.driver.current_url!=self.url):
            print('登陆成功')
        else:
            print('登录失败')
        time.sleep(5)
        self.driver.quit()
if __name__ == '__main__':
    login = Login()
    login.run()


