import unittest
from selenium import webdriver
from pageindex import PageIndex
from page_item_index import PageIndexItem


class IndexCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.IndexPage = PageIndex(self.driver)
        self.ItemIndexPage = PageIndexItem(self.driver)

    # Hacer busqueda con resultado exitoso(positivo)
    def test_search_existing_result(self):
        self.IndexPage.search_input('Printed')
        self.assertEqual(self.ItemIndexPage.return_existing_result(), '"PRINTED"')

    # Hacer busqueda sin resultado(negativo)
    def test_search_no_existent_result(self):
        self.IndexPage.search_input('hola')
        self.assertEqual(self.ItemIndexPage.return_no_results_text(), 'No results were found for your search "hola"')

        # Hacer busqueda sin resultado(negativo)
    def test_search_special_characters(self):
        self.IndexPage.search_input('??¿¿¿***///')
        self.assertEqual(self.ItemIndexPage.return_no_results_text(), 'No results were found for your search "??¿¿¿***///"')


