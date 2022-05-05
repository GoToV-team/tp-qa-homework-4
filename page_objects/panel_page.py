from page_objects.base import Page


class PanelPage(Page):
    PATH = 'creator-panel'
    CREATE_BUTTON = '.creator-panel__add-post > button'

    def open_creator(self):
        self._click_button(self.CREATE_BUTTON)
