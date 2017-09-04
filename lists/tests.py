from django.test import TestCase
from lists.models import Item


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        # Validate the correct template was used
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):

    def test_can_save_and_retrieve_data(self):
        first_item = Item()
        first_item.text = 'the first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'the second list item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, 'the first (ever) list item')
        self.assertEqual(second_saved_item.text, 'the second list item')
