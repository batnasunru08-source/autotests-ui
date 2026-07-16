import pytest
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.RegistrationFormComponent.fill(email="user.name@gmail.com", username="user", password="password")
    registration_page.RegistrationFormComponent.check_visible(email="user.name@gmail.com", username="user", password="password")
    registration_page.click_registration_form_button()
    dashboard_page.DashboardToolbarViewComponent.check_visible()
    dashboard_page.students_chart_view.check_visible('Students')
    dashboard_page.activities_chart_view.check_visible('Activities')
    dashboard_page.courses_chart_view.check_visible('Courses')
    dashboard_page.scores_chart_view.check_visible('Scores')