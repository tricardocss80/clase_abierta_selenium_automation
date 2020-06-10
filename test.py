# Sitio: http://automationpractice.com/index.php
# 1-Buscar por T-shirts
# 2-Al elemento que aparece, le clickean el color naranja
# 3-Poner 25 en cantidad
# 4-Clickear 3 veces el boton +
# 5-Verificar que el numero que aparece es 28

import unittest
from selenium import webdriver
from pageindex import Pageindex
from pageitems import Pageitems
from pageitem import Pageitem
import time


class SearchCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.IndexPage = Pageindex(self.driver)
        self.ItemsPage = Pageitems(self.driver)
        self.ItemPage = Pageitem(self.driver)
        self.driver.implicitly_wait(5)

    def test_tshirts_quantity(self):
        self.IndexPage.search('t-shirts')
        self.ItemsPage.click_button_orange()
        self.ItemPage.enter_quantity('25')
        self.ItemPage.add_elements(3)
        number = self.ItemPage.get_number_of_element()
        self.assertEqual(number, '28')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
