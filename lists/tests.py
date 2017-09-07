from django.test import TestCase
from lists.models import Item


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        # Validate the correct template was used
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_POST_request(self):
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')


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


class ListViewTest(TestCase):

    def test_displays_all_items(self):

        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

    def test_uses_list_view_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')


class NewListTest(TestCase):

    class_item_text = 'NewListCLass - New list item'

    # def post_new_data(self):
    #     return self.client.post('/list/new', data={'item_text': self.class_item_text})

    def test_can_save_a_post_request(self):
        # self.post_new_data()
        self.client.post('/lists/new', data={'item_text': 'test'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'test')

    def test_redirects_after_post(self):
        response = self.client.post('/lists/new', data={'item_text': 'test'})
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')







