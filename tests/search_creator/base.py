import unittest

from page_objects.user_page import UserPage
# from page_objects.search_page import SearchPage
from setup.default_setup import default_setup


class BaseSearchTest(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self):
        default_setup(self)

        self.start_page = UserPage(self.driver)

        self.start_page.open()

    def tearDown(self):
        self.start_page.open()

        self.driver.quit()
