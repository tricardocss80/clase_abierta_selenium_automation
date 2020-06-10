from selenium.webdriver.support.ui import Select
import time


class PageRegister:
    def __init__(self, my_driver):
        self.butoon_sin_in = "//a[@class='login']"
        self.input_email = "//input[@name='email_create']"
        self.button_create_an_account = "//form[@id='create-account_form']//span[1]"
        self.input_radio_mr = "//input[@type='radio'][contains(@id,'gender1')]"
        self.input_first_mame = "//input[@name='customer_firstname']"
        self.input_last_name = "//input[@name='customer_lastname']"
        self.input_email_creaded = 'email'
        self.input_pass = "//input[@type='password']"
        self.selec_days = "//select[@name='days']"
        self.selec_months = "//select[@name='months']"
        self.selec_yaars = "//select[@name='years']"
        self.cheakbox_newsletter = "//input[@name='newsletter']"
        self.input_first_name_address = "//input[@name='firstname']"
        self.input_company = "//input[@name='company']"
        self.input_company_address = "//input[@name='address1']"
        self.input_city = "//input[@name='city']"
        self.input_state = "//select[@name='id_state']"
        self.input_zip = "//input[contains(@name,'postcode')]"
        self.input_country = "//select[@name='id_country']"
        self.input_mobile_fone = "//input[@name='phone_mobile']"
        self.input_my_alias = "//input[@name='alias']"
        self.button_register = "//span[contains(.,'Register')]"
        self.driver = my_driver

    def button_log_in(self):
        self.driver.find_element_by_xpath(self.butoon_sin_in).click()
        time.sleep(3)

    def mail_register(self, item):
        self.driver.find_element_by_xpath(self.input_email).clear()
        self.driver.find_element_by_xpath(self.input_email).send_keys(item)
        self.driver.find_element_by_xpath(self.button_create_an_account).click()
        time.sleep(3)

    def form_register(self, data):
        self.driver.find_element_by_xpath(self.input_radio_mr).click()
        self.driver.find_element_by_xpath(self.input_first_mame).clear()
        self.driver.find_element_by_xpath(self.input_first_mame).send_keys(data['first_name'])
        self.driver.find_element_by_xpath(self.input_last_name).clear()
        self.driver.find_element_by_xpath(self.input_last_name).send_keys(data['last_name'])
        self.driver.find_element_by_id(self.input_email_creaded).click()
        self.driver.find_element_by_xpath(self.input_pass).clear()
        self.driver.find_element_by_xpath(self.input_pass).send_keys(data['Password'])
        Select(self.driver.find_element_by_xpath(self.selec_days)).select_by_value(data['day'])
        Select(self.driver.find_element_by_xpath(self.selec_months)).select_by_value(data['month'])
        Select(self.driver.find_element_by_xpath(self.selec_yaars)).select_by_value(data['year'])
        self.driver.find_element_by_xpath(self.cheakbox_newsletter).click()
        self.driver.find_element_by_xpath(self.input_first_name_address).clear()
        self.driver.find_element_by_xpath(self.input_first_name_address).send_keys(data['first_name_dress'])
        self.driver.find_element_by_xpath(self.input_company).clear()
        self.driver.find_element_by_xpath(self.input_company).send_keys(data['company'])
        self.driver.find_element_by_xpath(self.input_company_address).clear()
        self.driver.find_element_by_xpath(self.input_company_address).send_keys(data['address'])
        self.driver.find_element_by_xpath(self.input_city).clear()
        self.driver.find_element_by_xpath(self.input_city).send_keys(data['city'])
        Select(self.driver.find_element_by_xpath(self.input_state)).select_by_value(data['state'])
        self.driver.find_element_by_xpath(self.input_zip).clear()
        self.driver.find_element_by_xpath(self.input_zip).send_keys(data['zip'])
        Select(self.driver.find_element_by_xpath(self.input_country)).select_by_value(data['country'])
        self.driver.find_element_by_xpath(self.input_mobile_fone).clear()
        self.driver.find_element_by_xpath(self.input_mobile_fone).send_keys(data['movile'])
        self.driver.find_element_by_xpath(self.input_my_alias).clear()
        self.driver.find_element_by_xpath(self.input_my_alias).send_keys(data['my_alias'])
        self.driver.find_element_by_xpath(self.button_register).click()

