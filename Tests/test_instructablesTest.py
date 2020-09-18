from Pages.instructables_classes import instructables_classes
from Pages.instructables_course import instructables_course
from Pages.instructables_homepage import instructables_homepage
from Pages.instructables_login_redirect import instructables_login_redirect
from Utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_Login_CompleteQuiz(self):

        homepage = instructables_homepage(self.driver)
        search_page = instructables_classes(self.driver)
        login_page = instructables_login_redirect(self.driver)
        course_page = instructables_course(self.driver)

        homepage.access_homepage_and_scroll()

        search_page.search_and_find_class()

        login_page.login_user()

        course_page.look_at_a_lesson()


