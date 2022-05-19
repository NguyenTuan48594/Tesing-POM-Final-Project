
import sys
import time
import unittest

from pageObjects.LoginPage import LoginPage

class TestLoginPage():

    username = "48594"
    password = "0982276805"

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def test_function_login(self):
        self.login_page.setUserName(self.username)
        time.sleep(1)
        self.login_page.setPassword(self.password)
        time.sleep(1)
        self.login_page.clickLogin()
        time.sleep(1)
