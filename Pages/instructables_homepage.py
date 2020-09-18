from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pyhtmlreport import Report
from Utilities.BaseClass import BaseClass


class instructables_homepage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.report = Report()

    classes_diy = (By.CSS_SELECTOR, 'div[class="category-landing-classes-class"]')
    class_header = (By.CSS_SELECTOR, 'div[class="course-header-content"]')
    qa_question = (By.CSS_SELECTOR, 'div[class="qa-module qa-container"]')
    qa_list = (By.CSS_SELECTOR, 'li[class*="qa-question-item"]')
    list_body_expanded = (By.XPATH, '//li[@class="qa-question-item expanded"]//div[@class="qa-post-body"]')
    back_all_classes = (By.CSS_SELECTOR, 'a[class="btn btn-lg btn-large btn-yellow"]')

    def all_classes(self):
        return self.driver.find_element(*instructables_homepage.back_all_classes)

    def list_body_opened(self):
        return self.driver.find_element(*instructables_homepage.list_body_expanded)

    def questions_list(self):
        return self.driver.find_elements(*instructables_homepage.qa_list)

    def question_block(self):
        return self.driver.find_element(*instructables_homepage.qa_question)

    def instr_classes(self):
        return self.driver.find_elements(*instructables_homepage.classes_diy)

    def instr_classes_header(self):
        return self.driver.find_element(*instructables_homepage.class_header)

    def access_homepage_and_scroll(self):

        self.scroll_down(4)
        self.instr_classes()[1].click()

        self.wait_for_presence_of_element(self.class_header)
        self.highlight(self.instr_classes_header())

        self.scroll_down(12)

        self.driver.execute_script("arguments[0].scrollIntoView(true);" + "window.scrollBy(0,-100);",
                                   self.question_block())

        self.highlight(self.question_block())
        # self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", self.question_block())

        # self.actions.move_to_element(self.qa_question).perform()

        for i in range(3):
            self.questions_list()[i].click()
            sleep(1)
            self.wait_for_presence_of_element(self.list_body_expanded)

            i += 1

        self.scroll_down(5)

        self.scroll_into_view(self.all_classes())
        self.highlight(self.all_classes())

        self.all_classes().click()
