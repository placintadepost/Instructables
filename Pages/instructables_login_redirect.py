from time import sleep

from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class instructables_login_redirect(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    user = (By.CSS_SELECTOR, 'input[placeholder="Username"]')
    password = (By.CSS_SELECTOR, 'input[placeholder="Password"]')
    login_btn = (By.CSS_SELECTOR, 'button[class*="login"]')

    def user_field(self):
        return self.driver.find_element(*instructables_login_redirect.user)

    def pass_field(self):
        return self.driver.find_element(*instructables_login_redirect.password)

    def login_button(self):
        return self.driver.find_element(*instructables_login_redirect.login_btn)

    def login_user(self):
        self.wait_for_visibility(self.user)
        sleep(2)
        self.highlight(self.user_field())
        self.user_field().send_keys('apple_diet_pie')
        self.highlight(self.pass_field())
        self.pass_field().send_keys('QAZxsw123')
        self.highlight(self.login_button())
        self.login_button().click()