from components.level_card import LevelCard
from components.level_form import LevelForm
from page_objects.base import Page


class PostAddPage(Page):
    PATH = 'post/create'

    POST_SAVE_BUTTON = '.editor__save-panel button.btn_success'
    POST_TITLE = '.editor__title'
    POST_DESCRIPTION = '.editor__description'

    def __init__(self, driver):
        super().__init__(driver)
    
    def save(self):
        self._click_button(self.POST_SAVE_BUTTON)

    def fill_form(self, title, description):
        self._set_text(self.POST_TITLE, title)
        self._set_text(self.POST_DESCRIPTION, description)