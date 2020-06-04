# Sitio: http://automationpractice.com/index.php
# 1-Buscar por T-shirts
# 2-Al elemento que aparece, le clickean el color naranja
# 3-Poner 25 en cantidad
# 4-Clickear 3 veces el boton +
# 5-Verificar que el numero que aparece es 28

import unittest
from selenium import webdriver
import time
from pageindex import Pageindex
from pageitem import Pageitem


class SearchCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.IndexPage = Pageindex(self.driver)
        self.ItemPage = Pageitem(self.driver)

    def test_our_price_display(self):
        self.IndexPage.search('t-shirts')
        time.sleep(2)
        self.IndexPage.quantity('25')
        self.assertEqual(self.ItemPage.return_input_quantity_text(), '28')
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
