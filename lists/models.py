from django.db import models
from django.utils import timezone


class Item(models.Model):

	# We are giving the text field a default via a keyword argument.
	# You're adding arguments to your methods when you're calling them, but you give a name to those arguments.
	text = models.TextField(default='')

	# works similarly to .DateField, but adds time
	created_on = models.DateTimeField(auto_now_add=True)
	modified_on = models.DateTimeField(auto_now=True)

	def tags(self):
		# _set is a reverse relation
		# looking at all of that which is related to me
		return ', '.join(tag.tag_name for tag in self.tag_set.all())
		# <model>_set gets the <model> that is related to this class (Item)

	# It's important to have a default value especially if you already have an existing application
	# (we've seen it before when we initially had existing migrations).
	# We changed the application because there was an error saying that we needed to add a default option.
	#is_active = models.BooleanField(default='')

	# max_length is a required option.
	# default='' is an empty string.
	# blank=True allows the title to be blank.
	#title = models.CharField(max_length=100, default='', blank=True)

	# Every time an instance is saved, auto_now would change the value of the timestamp.
	#modified_on = models.DateField(auto_now=True)
	#created_on = models.DateField(auto_now_add=True)

	# example: 24.05
	#hours_done = models.DecimalField(max_digits=4, decimal_places=2)

	# essentially a CharField with email validation
	#fieldname = models.EmailField(max_length=255)

	# used for storing integer values
	#fieldname = models.IntegerField()


class Tag(models.Model): # let's say we want to organize our tasks
	tag_name = models.CharField(max_length=100)

	# used for assigning a many-to-one relationship / many tags to one task
	# first argument --> string representation of the model that we are creating a foreign key for
	# second argument --> so that Django will know what will happen if this instance were to be deleted
	tagged_item = models.ForeignKey('Item', on_delete=models.CASCADE)