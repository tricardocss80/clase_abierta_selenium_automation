import unittest
from selenium import webdriver
from page_login import PageLogin
from page_item_login import PageLoginItem


class LoginCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.LoginPage = PageLogin(self.driver)
        self.ItemLoginPage = PageLoginItem(self.driver)

    # Hacer login email existente y contraseña valida(positivo)
    def test_login_valid(self):
        data = {'email': 'riki805@gmail.com', 'password': 'velezcapo'}
        self.LoginPage.button_log_in()
        self.LoginPage.input_login_data(data)
        self.assertEqual(self.ItemLoginPage.return_assert_title_page(), 'Login - My Store')
        self.LoginPage.log_out()

    # Hacer login con email no exstente y contraseña valida(negativo)
    def test_login_user_no_exist(self):
        data = {
            'email': 'riki800@gmail.com',
            'password': 'velezcapo'
        }
        self.LoginPage.button_log_in()
        self.LoginPage.input_login_data(data)
        self.assertEqual(self.ItemLoginPage.return_block_error(), 'There is 1 error')
        self.assertEqual(self.ItemLoginPage.return_block_error_login(), 'Authentication failed.')

    # Hacer login con email invalido y contraseña valida(negativo)
    def test_login_email_invalid(self):
        data = {
            'email': 'riki800gmail.com',
            'password': 'velezcapo'
        }
        self.LoginPage.button_log_in()
        self.LoginPage.input_login_data(data)
        self.assertEqual(self.ItemLoginPage.return_block_error(), 'There is 1 error')
        self.assertEqual(self.ItemLoginPage.return_block_error_login(), 'Invalid email address.')

    # Hacer login sin email y contraseña valida(negativo)
    def test_login_without_email(self):
        data = {
            'email': '',
            'password': 'velezcapo'
        }
        self.LoginPage.button_log_in()
        self.LoginPage.input_login_data(data)
        self.assertEqual(self.ItemLoginPage.return_block_error(), 'There is 1 error')
        self.assertEqual(self.ItemLoginPage.return_block_error_login(), 'An email address required.')

    # Hacer login con email existente y contraseña inexistente(negativo)
    def test_login_without_pass(self):
        data = {
            'email': 'riki8054@gmail.com',
            'password': ''
        }
        self.LoginPage.button_log_in()
        self.LoginPage.input_login_data(data)
        self.assertEqual(self.ItemLoginPage.return_block_error(), 'There is 1 error')
        self.assertEqual(self.ItemLoginPage.return_block_error_login(), 'Password is required.')

    # Hacer login con email existente y contraseña invalida(negativo)
    def test_invalid_login_pass(self):
        data = {
            'email': 'riki8054@gmail.com',
            'password': 've'
        }
        self.LoginPage.button_log_in()
        self.LoginPage.input_login_data(data)
        self.assertEqual(self.ItemLoginPage.return_block_error(), 'There is 1 error')
        self.assertEqual(self.ItemLoginPage.return_block_error_login(), 'Invalid password.')

    # Hacer login sin datos(negativo)
    def test_login_without_data(self):
        data = {
            'email': '',
            'password': ''
        }
        self.LoginPage.button_log_in()
        self.LoginPage.input_login_data(data)
        self.assertEqual(self.ItemLoginPage.return_block_error(), 'There is 1 error')
        self.assertEqual(self.ItemLoginPage.return_block_error_login(), 'An email address required.')

    # Hacer login con email invalido y contraseña invalida(negativo)
    def test_login_with_invalid_data(self):
        data = {
            'email': 'riki800gmail.com',
            'password': 've'
        }
        self.LoginPage.button_log_in()
        self.LoginPage.input_login_data(data)
        self.assertEqual(self.ItemLoginPage.return_block_error(), 'There is 1 error')
        self.assertEqual(self.ItemLoginPage.return_block_error_login(), 'Invalid email address.')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()