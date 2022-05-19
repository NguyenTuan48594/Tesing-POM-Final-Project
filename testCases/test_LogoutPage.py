
import sys
import time
import unittest

from pageObjects.LogoutPage import LogoutPage

class TestLogOutPage():

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LogoutPage(driver)

    def test_function_logout(self):
        self.login_page.clickLogout()
        time.sleep(2)
        self.login_page.clickLogout1()
        time.sleep(2)

