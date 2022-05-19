import time
import unittest
import HtmlTestRunner
from selenium import webdriver
import sys

sys.path.append("D:/Desktop_files/Document_Basic/Testing/PythonFinalTestPOM")

from testCases.test_LoginPage import TestLoginPage
from testCases.test_NotifyPage import TestNotifyPage
from testCases.test_LogoutPage import TestLogOutPage

class MovieTest(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="D:\\Desktop_files\\Document_Basic\\Testing\\PythonFinalTestPOM\\drivers\\chromedriver.exe")
    baseURL = "https://my.uda.edu.vn/sv/svlogin"

    test_login_page = TestLoginPage(driver)
    test_notify_page = TestNotifyPage(driver)
    test_logout_page = TestLogOutPage(driver)

    driver.get(baseURL)
    driver.maximize_window()

    def test_movie_play(self):
        self.test_login_page.test_function_login()
        time.sleep(2)
        self.test_notify_page.test_function_notify()
        time.sleep(2)
        self.test_logout_page.test_function_logout()
        time.sleep(2)
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))