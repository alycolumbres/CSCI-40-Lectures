from django.conf.urls import url

from .views import HomeView, TaskListView, TaskCreateView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^tasks$', TaskListView.as_view(), name='task-list'),
	url(r'^tasks/new$', TaskCreateView.as_view(), name='task_create')
]