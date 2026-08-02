import pytest
import allure
from allure_commons.types import Severity

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION) # Добавили теги
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.AUTHENTICATION) # Добавили feature
@allure.story(AllureStory.REGISTRATION) # Добавили story
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    def test_successful_registration(self, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form_component.fill(email="user.name@gmail.com", username="user",
                                                           password="password")
        registration_page.registration_form_component.check_visible(email="user.name@gmail.com", username="user",
                                                                    password="password")
        registration_page.click_registration_form_button()
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.students_chart_view.check_visible('Students')
        dashboard_page.activities_chart_view.check_visible('Activities')
        dashboard_page.courses_chart_view.check_visible('Courses')
        dashboard_page.scores_chart_view.check_visible('Scores')