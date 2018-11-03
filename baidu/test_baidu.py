#coding=utf-8
'''
调用page页面
'''

from selenium import webdriver
from baidu.baidu_page import BaiduPage

dr = webdriver.Chrome()
page = BaiduPage(dr)
page.get("https://www.baidu.com")
page.search_box.send_keys("helel")
page.search_button.click()






