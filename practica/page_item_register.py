class PageRegisterItem:

    def __init__(self, my_driver):
        self.no_results_banner = "//*[@id='create_account_error']/ol/li"
        self.block_error = "//*[@id='center_column']/div/p"
        self.input_first_mame = "//*[@id='center_column']/div/ol/li[2]"
        self.input_last_name = "//*[@id='center_column']/div/ol/li[1]"
        self.input_pass = "//*[@id='center_column']/div/ol/li[3]"
        self.input_address = "//*[@id='center_column']/div/ol/li[4]"
        self.title_page = '/html/head/title'
        self.block_error_login_authentication = '//*[@id="center_column"]/div[1]/ol/li'

        self.driver = my_driver

    def return_no_elements_text(self):
        return self.driver.find_element_by_xpath(self.no_results_banner).text

    def return_block_error(self):
        return self.driver.find_element_by_xpath(self.block_error).text

    def return_assert_last_name(self):
        return self.driver.find_element_by_xpath(self.input_last_name).text

    def return_assert_first_name(self):
        return self.driver.find_element_by_xpath(self.input_first_mame).text

    def return_assert_pass(self):
        return self.driver.find_element_by_xpath(self.input_pass).text

    def return_assert_address(self):
        return self.driver.find_element_by_xpath(self.input_address).text

