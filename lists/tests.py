from django.test import TestCase

from .models import Item # importing the item class from the models module/models.py file


class HomePageTest(TestCase):

	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')
	# tests if homepage can handle a POST request
	def test_can_save_POST_request(self):
		response = self.client.post('/', data={
			'item_text': 'A new list item'
		})
		self.assertIn('A new list item', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')

# class ListPageTest(TestCase):

# 	def test_list_page_returns_correct_html(self):
# 		response = self.client.get('/tasks')
# 		self.assertTemplateUsed(response, 'task_list.html')


# class CreatePageTest(TestCase):

# 	def test_create_page_returns_correct_html(self):
# 		response = self.client.get('/tasks/new')
# 		self.assertTemplateUsed(response, 'task_create_form.html')
# classes --> database tables | class attributes --> database fields (columns) | instances of classes --> individual records (rows) of the database table
# To test models, we need to assume what the database should contain. This is because we haven't created our models yet. Ideally, database design documents are created first before any development happens.
class ItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		first_item = Item() # instantiating a new item / creating instances of the item class
		first_item.text = 'First Item' # setting this item's text attribute to be equal to 'First Item' / give that instance a text attribute with a string
		first_item.save() # saving this instance / saving this to the database using a save method

		second_item = Item()
		second_item.text = 'Second Item'
		second_item.save()
		# all models have a manager that handles the creation of querysets (collection of objects from the database), and the default is called objects
		items = Item.objects.all() # get all items/records / To test that it does work, and that we are able to retrieve it, we use item.objects.all()
		self.assertEqual(items.count(), 2) # assert that we have 2 items in the database

		saved_item_one = items[0] # get the individual items
		saved_item_two = items[1]

		self.assertEqual(saved_item_one.text, 'First Item') # tests if the test detects if the saved item is equal to what we expect it to be
		self.assertEqual(saved_item_two.text, 'Second Item')