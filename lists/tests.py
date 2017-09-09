from django.test import TestCase
from lists.models import Item, List


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ListAndItemModelTest(TestCase):

    def test_can_save_and_retrieve_data(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'the first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'the second list item'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, 'the first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'the second list item')
        self.assertEqual(second_saved_item.list, list_)


class ListViewTest(TestCase):

    def test_displays_only_shows_items_for_that_list(self):

        first_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=first_list)
        Item.objects.create(text='itemey 2', list=first_list)

        other_list = List.objects.create()
        Item.objects.create(text='fuckeroo 1', list=other_list)
        Item.objects.create(text='fuckeroo 2', list=other_list)

        response = self.client.get(f'/lists/{first_list.id}/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'fuckeroo 1')
        self.assertNotContains(response, 'fuckeroo 2')


    def test_passes_proper_list_to_temlplate(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.get(f'/lists/{correct_list.id}/')

        self.assertEqual(response.context['list'], correct_list)


    def test_uses_list_view_template(self):
        list_ = List.objects.create()
        response = self.client.get(f'/lists/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')


class NewListTest(TestCase):

    class_item_text = 'NewListCLass - New list item'

    def test_can_save_a_post_request(self):
        self.client.post('/lists/new', data={'item_text': 'test'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'test')

    def test_redirects_after_post(self):
        response = self.client.post('/lists/new', data={'item_text': 'test'})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')

    def test_can_save_a_POST_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'from new item test class'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'from new item test class')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'add a damn item'})

        self.assertRedirects(response, f'/lists/{correct_list.id}/')










