from django.conf.urls import url, include

from rest_framework import routers

from .views import HomeView, TaskDetailView, TaskListView, TaskCreateView, ItemViewSet

router = routers.DefaultRouter()
# Here's where we're going to add the base URL for the viewset.
# basically the name of our resource
router.register(r'items', ItemViewSet)

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^tasks$', TaskListView.as_view(), name='task-list'),
	url(r'^tasks/new$', TaskCreateView.as_view(), name='task_create'),
	# url that will point to an individual instance
	# will accept an id as an argument, which means we will create a regular expression
	# ?P<id> --> python knows this is an id
	# [0-9]+ --> id is going to be a numeric key or a numeric string for as long as it needs to be
	url(r'^task/(?P<id>[0-9]+)$', TaskDetailView.as_view(), name='task_detail'),
	url(r'', include(router.urls)) # '' empty because it will use 'items'
]