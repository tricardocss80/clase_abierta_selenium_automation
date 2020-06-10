from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Pageindex:
    def __init__(self, my_driver):
        self.query_top = (By.XPATH, '//*[@id="search_query_top"]')
        self.query_button = (By.XPATH, '//*[@id="searchbox"]/button')
        self.driver = my_driver

    def search(self, item):
        search_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.query_top))
        search_input.send_keys(item)
        search_button = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.query_button))
        search_button.click()
