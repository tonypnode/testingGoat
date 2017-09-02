from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')

        # Make sure it's an html document
        self.assertTrue(html.startswith('<html'))

        # Make sure that shits in the title
        self.assertIn('<title>To-Do-Lists</title>', html)

        # Make sure it ends with html, but I don't think this is really needed
        self.assertTrue(html.strip().endswith('/html>'))

        # Validate the correct template was used
        self.assertTemplateUsed(response, 'home.html')



