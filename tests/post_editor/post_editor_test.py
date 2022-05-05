import os

from setup.default_setup import default_setup
from tests.post_editor.base import BasePostEditorTest


class PostEditorTest(BasePostEditorTest):
    TITLE = 'HELLO WORLD'
    DESCRIPTION = 'Description'

    # def __init__(self, methodName: str = ...):
    #     super(PostEditorTest, self).__init__(methodName)

    # def setUp(self):
    #     super().setUp()
    #     default_setup(self)

    # def tearDown(self):
    #     super().tearDown()

    def test_no_data(self):
        self.page.fill_form('','')
        self.page.save()

        self.assertEqual(self.page.driver.current_url.replace('https://pyaterochka-team.site/', ''), self.page.PATH)
    
    def test_correct_data(self):
        self.page.fill_form(self.TITLE, self.DESCRIPTION)
        self.page.save()
        

        t,d = self.edit_page.get_form()
        self.assertEqual(t, self.TITLE)
        self.assertEqual(d, self.DESCRIPTION)



        


