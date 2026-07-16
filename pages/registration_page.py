from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_button = page.get_by_test_id("registration-page-registration-button")

        self.RegistrationFormComponent = RegistrationFormComponent(page)

    def click_registration_form_button(self):
        self.registration_button.click()




