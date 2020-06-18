from django.contrib import admin

from .models import Item, Tag


# Inline ModelAdmins provide a way to create or edit models that have a foreign key to that current model.
# Inlines extend specific classes that would create inline classes.
class TagInlineAdmin(admin.TabularInline): # or StackedInline
	model = Tag


# registers admin to say that the Item model will use ItemAdmin as its default admin
# @admin.register(Item) --> decorator
class ItemAdmin(admin.ModelAdmin): # handler for a specific admin view
	model = Item

	# if you want to display other properties of an item --> list_display attribute
	# created_on values are default (in video) --> not necessarily the time you made the item
	list_display = ('text', 'created_on', 'modified_on', 'tags')

	# 'fields' property on the ModelAdmin takes in a list
	#fields = [ # displayed per row (so 3 rows, 2 field in 2nd row)
	#	'text',
	#	('created_on', 'modified_on'),
	#	'tags'
	#]
	# doesn't work lmao

	# another property that can edit the details view
	# if you want to have a nicer view after your code gets more complicated
	fieldsets = (
		(
			'Basic Information', { 'fields': ('text',) } # key-value pair/dictionary --> contains the 'fields' keyword and a list of all the fields that should go in there
		), # extra commas because it must be a list
	)

	# to add TagInlineAdmin to ItemAdmin
	# 'inlines' property takes in a list of the inlines that we are using
	inlines = [TagInlineAdmin, ]

# (lines 8 and 11) another way to register other than using a decorator
admin.site.register(Item, ItemAdmin)