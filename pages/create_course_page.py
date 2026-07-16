from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.navigation.navbar_component import NavbarComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')

        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')

        self.CreateCourseExercisesToolbarViewComponent = CreateCourseExercisesToolbarViewComponent(page)

        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

        self.CreateCourseFormComponent = CreateCourseFormComponent(page)

        self.CreateCourseToolbarViewComponent = CreateCourseToolbarViewComponent(page)

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )