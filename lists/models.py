from django.db import models


class Item(models.Model):
	text = models.TextField(default='') # We are giving the text field a default via a keyword argument. / You're adding arguments to your methods when you're calling them, but you give a name to those arguments.