from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Pageitems:
    def __init__(self, my_driver):
        self.orange_button = (By.XPATH, '//*[@id="color_1"]')
        self.driver = my_driver

    def click_button_orange(self):
        button_orange = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.orange_button))
        button_orange.click()
