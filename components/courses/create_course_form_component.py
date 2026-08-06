import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title_input = Input(page, 'create-course-form-title-input', 'Create Course Title')
        self.create_course_estimated_time_input = Input(page, 'create-course-form-estimated-time-input', 'Create Course Estimated Time')
        self.create_course_description_textarea = Textarea(page,'create-course-form-description-input', 'Create Course Description')
        self.create_course_max_score_input = Input(page, 'create-course-form-max-score-input', 'Create Course Max Score')
        self.create_course_min_score_input = Input(page, 'create-course-form-min-score-input', 'Create Course Min Score')

    @allure.step("Fill create course form {title}, {description}, {estimated_time}, {max_score}, {min_score}")
    def fill(self, title, estimated_time, description, max_score, min_score):
        self.create_course_title_input.fill(title)

        self.create_course_estimated_time_input.fill(estimated_time)

        self.create_course_description_textarea.fill(description)

        self.create_course_max_score_input.fill(max_score)

        self.create_course_min_score_input.fill(min_score)

    @allure.step("Check visible course form {title}, {description}, {estimated_time}, {max_score}, {min_score}  ")
    def check_visible(self, title, estimated_time, description, max_score, min_score):
        self.create_course_title_input.check_visible()
        self.create_course_title_input.check_have_value(title)

        self.create_course_estimated_time_input.check_visible()
        self.create_course_estimated_time_input.check_have_value(estimated_time)

        self.create_course_description_textarea.check_visible()
        self.create_course_description_textarea.check_have_value(description)

        self.create_course_max_score_input.check_visible()
        self.create_course_max_score_input.check_have_value(max_score)

        self.create_course_min_score_input.check_visible()
        self.create_course_min_score_input.check_have_value(min_score)
