import logging
import time
import webbrowser
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.pyrobot import Robot, Keys


def openWindow():
    bot = Robot()
    bot.key_press(Keys.ctrl)
    bot.key_press(Keys.shift)
    bot.key_press(Keys.n)
    bot.key_release(Keys.ctrl)
    bot.key_release(Keys.shift)
    bot.key_release(Keys.n)


@pytest.mark.usefixtures("setup")
class BaseClass:

    def highlight(self, element, effect_time=1.3, color="yellow", border=5):
        driver = element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  element, s)

        original_style = element.get_attribute('style')
        apply_style("border: {0}px solid {1};".format(border, color))
        time.sleep(effect_time)
        apply_style(original_style)

    @staticmethod
    def open_window(url):
        path = r'C:\\Users\\OlGGa\\AppData\\Local\\Programs\\Opera\\69.0.3686.57\\opera.exe'
        webbrowser.get(path).open_new(url)

    def wait_for_text_match(self, element, text):
        WebDriverWait(self, 20).until(
            EC.text_to_be_present_in_element(element, text))

    def wait_for_url_change(self, current_url):
        WebDriverWait(self, 20).until(
            EC.url_changes(current_url))

    def wait_for_presence_of_element(self, element):

        for i in range(10):

            try:
                WebDriverWait(self, 20).until(
                    EC.presence_of_element_located(element))

            except Exception:
                i += 1

    def wait_for_visibility(self, element):

        for i in range(10):

            try:
                WebDriverWait(self, 20).until(
                    EC.visibility_of_element_located(element))

            except Exception:
                i += 1

    def wait_for_invisibility(self, element):

        for i in range(10):

            try:
                WebDriverWait(self, 20).until(
                    EC.invisibility_of_element_located(element))

            except Exception:
                i += 1

    def wait_for_clickable(self, element):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(element))

    def click_element(self, element):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(element)).click()

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);" + "window.scrollBy(0,-100);",
                                   element)

    def action_chains(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def verifyItsDisplayed(self, a):

        locator = self.driver.find_element(a)

        if locator.is_displayed():
            print("Element is visible")
        else:
            print("Element isn't there")

    def handle(self, a):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[a])

    def getCurrentWindowHandle(self):
        handles = self.driver.window_handles
        size = len(handles)
        for x in range(size):
            if handles[x] != self.driver.current_window_handle:
                self.driver.switch_to.window(handles[x])

    def scroll_down(self, nr):
        scroll = .1
        while scroll < nr:
            self.driver.execute_script("window.scrollBy(0,3)", " ")
            scroll += .01

    def scroll_up(self, nr):
        scroll = .1
        while scroll < nr:
            self.driver.execute_script("window.scrollBy(0,-3)", " ")
            scroll += .01


