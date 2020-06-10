import time


class PageLogin:
    def __init__(self, my_driver):
        self.butoon_sin_in = "//a[@class='login']"
        self.input_email_login = '// *[ @ id = "email"]'
        self.input_pass_login = '// *[ @ id = "passwd"]'
        self.button_login = '//*[@id="SubmitLogin"]/span'
        self.button_log_out = '//*[@id="header"]/div[2]/div/div/nav/div[2]/a'
        self.driver = my_driver

    def button_log_in(self):
        self.driver.find_element_by_xpath(self.butoon_sin_in).click()
        time.sleep(3)

    def input_login_data(self, data):
        self.driver.find_element_by_xpath(self.input_email_login).clear()
        self.driver.find_element_by_xpath(self.input_email_login).send_keys(data['email'])
        self.driver.find_element_by_xpath(self.input_pass_login).clear()
        self.driver.find_element_by_xpath(self.input_pass_login).send_keys(data['password'])
        self.driver.find_element_by_xpath(self.button_login).click()

    def log_out(self):
        self.driver.find_element_by_xpath(self.button_log_out).click()
