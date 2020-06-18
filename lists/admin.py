from django.contrib import admin

from .models import Item, Tag

# registers admin to say that the Item model will use ItemAdmin as its default admin
# @admin.register(Item) --> decorator
class ItemAdmin(admin.ModelAdmin): # handler for a specific admin view
	model = Item

# (lines 8 and 11) another way to register other than using a decorator
admin.site.register(Item, ItemAdmin)