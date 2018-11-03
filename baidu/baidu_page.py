#coding=utf-8

class BasePage:
    '''
    基础page
    '''
    def __init__(self,driver):
        self.driver = driver

    def get(self,url):
        self.driver.get(url)

    def id_(self,id_):
        return self.driver.find_element_by_id(id_)

    def xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)

class BaiduPage(BasePage):
    '''
    百度首页page
    '''
    @property
    def search_box(self):
        return self.id_("kw")

    @property
    def search_button(self):
        return self.xpath("//*[@id='su']")



