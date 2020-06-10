class PageLoginItem:

    def __init__(self, my_driver):
        self.no_results_banner = "//*[@id='create_account_error']/ol/li"
        self.block_error = "//*[@id='center_column']/div/p"
        self.title_page = '/html/head/title'
        self.block_error_login_authentication = '//*[@id="center_column"]/div[1]/ol/li'
        self.driver = my_driver

    def return_block_error(self):
        return self.driver.find_element_by_xpath(self.block_error).text

    def return_assert_title_page(self):
        return self.driver.find_element_by_xpath(self.title_page).get_attribute('text')

    def return_block_error_login(self):
        return self.driver.find_element_by_xpath(self.block_error_login_authentication).text
