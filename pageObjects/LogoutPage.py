from selenium.webdriver import Keys


class LogoutPage():

    button_logout_id = "Hệ thống"
    button_logout1_idd = "Đăng xuất"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.button_logout_id).click()

    def clickLogout1(self):
        self.driver.find_element_by_link_text(self.button_logout1_idd).click()
