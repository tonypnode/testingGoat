from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_table_for_row_text(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_todo_stuff_works(self):
        self.browser.get(self.live_server_url)

        # page title mentions To-Do in the title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to enter a To do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item', 'YOU SHIT AINT GOT DAT SHIT')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        self.check_table_for_row_text('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        self.check_table_for_row_text('2: use peacock feathers to make a fly')

        time.sleep(2)
        self.check_table_for_row_text('1: Buy peacock feathers')
        self.check_table_for_row_text('2: use peacock feathers to make a fly')
