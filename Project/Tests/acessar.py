import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Adria/Desktop/Selenium/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_itau(self):
        self.driver.get("https://www.itau.com.br/")
        sleep(5)
        self.driver.find_element_by_id("agencia").send_keys("1234")
        self.driver.find_element_by_id("conta").send_keys("234125")
        self.driver.find_element_by_id("btnLoginSubmit").click()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
