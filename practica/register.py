import unittest
from selenium import webdriver
from page_register import PageRegister
from page_item_register import PageRegisterItem


class RegisterCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.RegisterPage = PageRegister(self.driver)
        self.RegisterItemPage = PageRegisterItem(self.driver)

    # Hacer un registro valido(Positivo)
    def test_register_new_user(self):
        email = 'rikiqa80@gmail.com'
        self.RegisterPage.button_log_in()
        self.RegisterPage.mail_register(email)
        data = {
            'first_name': 'riki',
            'last_name': 'taso',
            'Password': 'velezcapo',
            'day': '7',
            'month': '12',
            'year': '1980',
            'first_name_dress': 'lala',
            'company': 'vertice',
            'address': 'lafuente 3924',
            'city': 'Avellaneda',
            'state': '10',
            'zip': '30004',
            'country': '21',
            'movile': '1133965889',
            'my_alias': 'lafuente 3924'
        }

        self.RegisterPage.form_register(data)

    # probar email ya registrado(negativo)
    def test_existing_user_registration(self):
        email = 'rikiqa80@gmail.com'
        self.RegisterPage.button_log_in()
        self.RegisterPage.mail_register(email)
        self.assertEqual(self.RegisterItemPage.return_no_elements_text(),
                        'An account using this email address has already been registered. Please enter a valid password or request a new one.')

    # probar email invalodo(negativo)
    def test_invalid_email(self):
        email = ''
        self.RegisterPage.button_log_in()
        self.RegisterPage.mail_register(email)
        self.assertEqual(self.RegisterItemPage.return_no_elements_text(), 'Invalid email address.')

    # Hacer un registro invalido probando bloques de error(negativo)
    def test_check_all_error_blocks(self):
        email = 'riki8054@gmail.com'
        self.RegisterPage.button_log_in()
        self.RegisterPage.mail_register(email)

        data = {
            'first_name': '',
            'last_name': '',
            'Password': '',
            'day': '7',
            'month': '12',
            'year': '1980',
            'first_name_dress': 'lala',
            'company': 'vertice',
            'address': '',
            'city': 'Avellaneda',
            'state': '10',
            'zip': '30004',
            'country': '21',
            'movile': '1133965886',
            'my_alias': 'Lafuente 3924'
        }

        self.RegisterPage.form_register(data)

        self.assertEqual(self.RegisterItemPage.return_block_error(), 'There are 4 errors')
        self.assertEqual(self.RegisterItemPage.return_assert_last_name(), 'lastname is required.')
        self.assertEqual(self.RegisterItemPage.return_assert_first_name(), 'firstname is required.')
        self.assertEqual(self.RegisterItemPage.return_assert_pass(), 'passwd is required.')
        self.assertEqual(self.RegisterItemPage.return_assert_address(), 'address1 is required.')

        print('Se verificaron los textos deceados')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
