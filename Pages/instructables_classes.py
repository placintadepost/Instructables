
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Utilities.BaseClass import BaseClass


class instructables_classes(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    search_input = (By.CSS_SELECTOR, 'input[class="search-input"]')
    searched_classes = (By.CSS_SELECTOR, 'div[class="thumbnail class-thumbnail "]')
    header = (By.CSS_SELECTOR, 'div[class="course-header-content"]')
    download = (By.XPATH, '(//a[@id="download-pdf-btn"])[2]')

    def download_btn(self):
        return self.driver.find_element(*instructables_classes.download)

    def search(self):
        return self.driver.find_element(*instructables_classes.search_input)

    def search_result(self):
        return self.driver.find_elements(*instructables_classes.searched_classes)

    def header_modal(self):
        return self.driver.find_element(*instructables_classes.header)

    def search_and_find_class(self):
        self.wait_for_visibility(self.search_input)
        # sleep(2)
        self.highlight(self.search())
        self.click_element(self.search_input)
        self.search().send_keys('cooking')
        self.search().send_keys(Keys.ENTER)

        self.wait_for_visibility(self.searched_classes)
        self.wait_for_clickable(self.searched_classes)
        # sleep(2)
        self.highlight(self.search_result()[1])
        self.search_result()[1].click()
        self.wait_for_visibility(self.header)
        self.highlight(self.header_modal())
        # sleep(2)
        self.scroll_into_view(self.download_btn())
        self.highlight(self.download_btn())
        self.download_btn().click()
