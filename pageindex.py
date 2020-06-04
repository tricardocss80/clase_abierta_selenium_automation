import time


class Pageindex:
    def __init__(self, my_driver):
        self.query_top = 'search_query_top'
        self.query_button = 'submit_search'
        self.result_option_color = "//a[@id='color_1']"
        self.result_input_quantity = 'quantity_wanted'
        self.result_input_button_plus = "//i[contains(@class,'icon-plus')]"
        self.driver = my_driver

    def search(self, item):
        self.driver.find_element_by_id(self.query_top).send_keys(item)
        self.driver.find_element_by_name(self.query_button).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.result_option_color).click()

    def quantity(self, item):
        self.driver.find_element_by_id(self.result_input_quantity).clear()
        self.driver.find_element_by_id(self.result_input_quantity).send_keys(item)
        self.driver.find_element_by_xpath(self.result_input_button_plus).click()
        self.driver.find_element_by_xpath(self.result_input_button_plus).click()
        self.driver.find_element_by_xpath(self.result_input_button_plus).click()
        time.sleep(2)
