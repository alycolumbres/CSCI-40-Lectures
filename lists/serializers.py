from rest_framework import serializers

from .models import Tag, Item


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		# required
		model = Tag
		fields = '__all__'


class ItemSerializer(serializers.Serializer):
	# We want our serializer field names to be the same as our model field names.
	# If we want to use Django REST Framework to create items, blank text is fine because in our model field as well, we have a default of a string.
	text = serializers.CharField(allow_blank=True)
	# When we request our list of items, we want to be able to see all the tags.
	# Because this is a related field, we could just nest another serializer in here.
	# many=True --> many instances that could go here
	# read_only --> easier for us to create instances of our item, because if not read_only, for every time that we create an item, we have to create a tag
	tag_set = TagSerializer(many=True, read_only=True)


	class Meta:
		model = Item
		fields = ['text', 'tag_set']