from selenium.webdriver import Keys


class LoginPage():

    textbox_username_id = "//*[@id='User']"
    textbox_password_id = "//*[@id='Password']"
    button_login_id = "//*[@id='Lnew1']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_id).click()
