from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_todo_stuff_works(self):
        # TODO: what about 127.0.0.1? jacktard
        self.browser.get("http://localhost:8000")

        # page title mentions To-Do in the title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the Test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
