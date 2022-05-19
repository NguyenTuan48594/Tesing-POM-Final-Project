
import sys
import time
import unittest

from pageObjects.NotifyPage import NotifyPage

class TestNotifyPage():

    find = "Nội quy học đường"

    def __init__(self, driver):
        self.driver = driver
        self.login_page = NotifyPage(driver)

    def test_function_notify(self):
        self.login_page.clickNotify()
        time.sleep(1)
        self.login_page.clickNotify1()
        time.sleep(2)
        self.login_page.scrollNotify1()
        time.sleep(2)
        self.login_page.clickNotify()
        time.sleep(1)
        self.login_page.clickDocument()
        time.sleep(2)
        self.login_page.setFind(self.find)
        time.sleep(2)
        self.login_page.clickFind()
        time.sleep(2)
        self.login_page.clickFindButton()
        time.sleep(2)
        self.login_page.scrollDocument()
        time.sleep(2)

