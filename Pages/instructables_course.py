from time import sleep

from selenium.webdriver.common.by import By

from Utilities.BaseClass import BaseClass


class instructables_course(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    lesson_one = (By.XPATH, '(//div[@class="lesson-summary-wrapper"])[1]')
    lesson_one_btn = (By.XPATH, '(//div[@class="lesson-summary-wrapper"])[1]//a[@class="start-lesson-btn btn '
                                'btn-default"]')
    quiz_wrapper = (By.CSS_SELECTOR, 'div[class="quiz-module"]')
    quiz_toggle = (By.CSS_SELECTOR, 'label[class="radio"]')
    answer_btn = (By.CSS_SELECTOR, 'a[class*="quiz-answer-btn"]')

    answer = (By.XPATH, '//span[@class="success-notice"]')

    def answer_text(self):
        return self.driver.find_elements(*instructables_course.answer)

    def answer_button(self):
        return self.driver.find_elements(*instructables_course.answer_btn)

    def quiz_radio(self):
        return self.driver.find_elements(*instructables_course.quiz_toggle)

    def quiz_module(self):
        return self.driver.find_elements(*instructables_course.quiz_wrapper)

    def first_lesson_btn(self):
        return self.driver.find_element(*instructables_course.lesson_one_btn)

    def first_lesson(self):
        return self.driver.find_element(*instructables_course.lesson_one)

    def look_at_a_lesson(self):
        sleep(2)
        self.scroll_into_view(self.first_lesson())
        self.highlight(self.first_lesson())
        self.wait_for_clickable(self.lesson_one_btn)
        self.highlight(self.first_lesson_btn())
        self.first_lesson_btn().click()
        self.scroll_down(22)

        self.answer_questions()

    def answer_questions(self):
        answers = [2, 4, 6, 9]

        for i in range(4):
            self.scroll_into_view(self.quiz_module()[i])
            self.highlight(self.quiz_module()[i])
            sleep(1)
            self.quiz_radio()[answers[i]].click()
            self.answer_button()[i].click()
            sleep(1)

            i += 1

        assert self.answer_text()[
                   0].text == 'Correct! Knives with full tang offer better control, weight balance, and are less likely to break.'

        assert self.answer_text()[
                   1].text == "Correct! A steel doesn't add to a knife, it straightens the edge"

        assert self.answer_text()[
                   2].text == "Yes! With proper care cast iron pans can last for a very long time. They build up a layer of oil from previous uses which season the pan, so keeping them around for a long time only makes the food taste better!"

        assert self.answer_text()[
                   3].text == "Yes! In the sense that they all cook your food and amazing meals can be made on ANY heat source. Purists will have a preferred method, and you will, too. But, as long as the heat can cook your food, whatever you have to work with is just fine!"
