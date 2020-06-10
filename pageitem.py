from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Pageitem:
    def __init__(self, my_driver):
        self.input_quantity = (By.XPATH, '//*[@id="quantity_wanted"]')
        self.button_plus = (By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]/span/i')
        self.driver = my_driver

    def enter_quantity(self, quantity):
        input_quantity = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.input_quantity))
        input_quantity.clear()
        input_quantity.send_keys(quantity)

    def add_elements(self, quantity):
        for i in range(quantity):
            button_add_element = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.button_plus))
            button_add_element.click()

    def get_number_of_element(self):
        return self.driver.find_element(*self.input_quantity).get_attribute('value')