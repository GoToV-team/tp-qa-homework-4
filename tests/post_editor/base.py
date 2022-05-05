import unittest

from page_objects.author_settings_page import AuthorSettingsPage
from page_objects.post_add_page import PostAddPage
from page_objects.post_edit_page import PostEditPage
from page_objects.settings_page import SettingsPage
from page_objects.user_page import UserPage
from setup.default_setup import default_setup


class BasePostEditorTest(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self):
        default_setup(self)

        self.page = PostAddPage(self.driver)
        self.edit_page = PostEditPage(self.driver)
        
        self.page.open()        

    def tearDown(self):
        self.driver.quit()
