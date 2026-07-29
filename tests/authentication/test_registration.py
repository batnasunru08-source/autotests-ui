import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
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