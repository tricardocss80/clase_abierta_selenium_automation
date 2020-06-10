from selenium.webdriver.support.ui import Select
import time


class PageIndex:
    def __init__(self, my_driver):
        self.input_search = '//*[@id="search_query_top"]'
        self.search_button = '//*[@id="searchbox"]/button'
        self.driver = my_driver

    def search_input(self, item):
        self.driver.find_element_by_xpath(self.input_search).clear()
        self.driver.find_element_by_xpath(self.input_search).send_keys(item)
        self.driver.find_element_by_xpath(self.search_button).click()
        time.sleep(2)
