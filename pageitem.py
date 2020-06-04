class Pageitem:
    def __init__(self, my_driver):
        self.result_input_quantity = 'quantity_wanted'
        self.driver = my_driver

    def return_input_quantity_text(self):
        return self.driver.find_element_by_id(self.result_input_quantity).get_attribute('value')
