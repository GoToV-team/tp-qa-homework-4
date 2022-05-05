from components.level_card import LevelCard
from components.level_form import LevelForm
from page_objects.base import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PostEditPage(Page):
    POST_SAVE_BUTTON = '.editor__save-panel button.btn_success'
    POST_REMOVE_BUTTON = '.editor__save-panel button.btn_primary'

    POST_TITLE = '.editor__title'
    POST_DESCRIPTION = '.editor__description'

    def __init__(self, driver):
        super().__init__(driver)
    
    def save(self):
        self._click_button(self.POST_SAVE_BUTTON)

    def fill_title_form(self, title, description):
        self._set_text(self.POST_TITLE, title)
        self._set_text(self.POST_DESCRIPTION, description)

    def get_form(self):
        return self._get_element(self.POST_TITLE).text, self._get_element(self.POST_DESCRIPTION).text