from selenium.webdriver import Keys


class NotifyPage():

    button_notify_id = "Thông báo"
    button_notify1_id = "Thời khóa biểu"
    button_notify5_id = "Văn bản biểu mẫu"
    textbox_find_id = "//*[@id='MainContent_Tvb']"
    click_find_id = "//*[@id='MainContent_Lref1']"
    click_find_button = "//*[@id='MainContent_GV3_GVC2_2_c2_open_0']"

    def __init__(self, driver):
        self.driver = driver

    def setFind(self, text):
        self.driver.find_element_by_xpath(self.textbox_find_id).send_keys(text)

    def clickNotify(self):
        self.driver.find_element_by_link_text(self.button_notify_id).click()

    def clickNotify1(self):
        self.driver.find_element_by_link_text(self.button_notify1_id).click()

    def scrollNotify1(self):
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    def clickDocument(self):
        self.driver.find_element_by_link_text(self.button_notify5_id).click()

    def scrollDocument(self):
        self.driver.execute_script("window.scrollTo(0, 300)")

    def clickFind(self):
        self.driver.find_element_by_xpath(self.click_find_id).click()

    def clickFindButton(self):
        self.driver.find_element_by_xpath(self.click_find_button).click()

